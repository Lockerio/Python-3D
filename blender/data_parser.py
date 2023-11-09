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
    def get_objects_parameters_as_dict(obj):
        geo_nodes_mod  = None
        for mod in obj.modifiers:
            if mod.type == 'NODES':
                geo_nodes_mod = mod
                break

        if geo_nodes_mod:
            group_output = geo_nodes_mod.node_group.nodes.get("Group Output")

            if group_output:
                parameters = {
                    "Длина": group_output.inputs["Длина"].default_value,
                    "Ширина": group_output.inputs["Ширина"].default_value,
                    "Высота": group_output.inputs["Высота"].default_value
                }
        
        return parameters