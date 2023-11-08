import bpy

class Parser():
    @staticmethod
    def get_all_mesh_objects(all_objects):
        mesh_objects = []
        for object in all_objects:
            if object.type == "MESH":
                mesh_objects.append(object)
        return mesh_objects

    @staticmethod
    def get_objects_parameters_as_dict(elements):
        for element in elements:
            if element and element.bl_rna.identifier == "Object":
                object_name = element.name
                obj = bpy.data.objects.get(object_name)

                if obj and obj.geometry_nodes:
                    node_tree = obj.geometry_nodes
                    output_node = None

                    for node in node_tree.nodes:
                        if node.type == 'GROUP_OUTPUT':
                            output_node = node
                            break

                    if output_node:
                        parameters = {}

                        for input in output_node.inputs:
                            if input.links:
                                linked_socket = input.links[0].from_socket
                                if linked_socket.node:
                                    parameter_name = input.identifier
                                    parameter_value = linked_socket.node.label
                                    parameters[parameter_name] = parameter_value

                        print(f"Собранные параметры из узла Group Output для объекта '{object_name}':")
                        for key, value in parameters.items():
                            print(f"{key}: {value}")

                    else:
                        print(f"Узел Group Output не найден в Geometry Nodes для объекта '{object_name}'.")

                else:
                    print(f"Указанный объект '{object_name}' не имеет Geometry Nodes.")

            else:
                print("Активный элемент в Outliner-е не является объектом.")
