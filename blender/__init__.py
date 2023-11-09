bl_info = {
    'name': 'Get shape sizes',
    'category': 'All',
    'version': (0, 0, 1),
    'blender': (3, 6, 0)
}


import bpy
from .view import AddonPanel
from .operator import AddonOperator


def register():
    bpy.utils.register_class(AddonPanel)
    bpy.utils.register_class(AddonOperator)

def unregister():
    bpy.utils.unregister_class(AddonPanel)
    bpy.utils.unregister_class(AddonOperator)

if __name__ == "__main__":
    register()