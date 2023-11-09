import bpy
from .operator import AddonOperator


class AddonPanel(bpy.types.Panel):
    bl_label = "Get shape sizes"
    bl_idname = "PT_AddonPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator(AddonOperator.bl_idname, text="Get sizes")

