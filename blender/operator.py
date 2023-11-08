import bpy

from .parser import Parser

class AddonOperator(bpy.types.Operator):
    bl_idname = "wm.addon_operator"
    bl_label = "Моя кнопка"

    def execute(self, context):
        all_objects = bpy.data.objects
        mesh_objects = Parser.get_all_mesh_objects(all_objects)
        # objects_parameters = Parser.get_parameters_as_dict(mesh_objects)
        Parser.get_parameters_as_dict(mesh_objects)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(AddonOperator)

def unregister():
    bpy.utils.unregister_class(AddonOperator)
