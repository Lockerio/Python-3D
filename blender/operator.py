import bpy
import json

from .data_parser import Parser
from .manager import DataManager

class AddonOperator(bpy.types.Operator):
    bl_idname = "wm.addon_operator"
    bl_label = "Моя кнопка"

    def execute(self, context):
        visible_objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']

        data = {}
        for obj in visible_objects:
            parameters = Parser.get_objects_parameters_as_dict(obj)
            if parameters:
                data[obj.name] = parameters

        DataManager.save_objects_parameters_to_json(data, "1.json")
        return {'FINISHED'}
