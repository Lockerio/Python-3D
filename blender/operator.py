import bpy

class AddonOperator(bpy.types.Operator):
    bl_idname = "wm.addon_operator"
    bl_label = "Моя кнопка"

    def execute(self, context):
        # Ваш код для выполнения действия
        bpy.ops.object.text_add()
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(AddonOperator)

def unregister():
    bpy.utils.unregister_class(AddonOperator)
