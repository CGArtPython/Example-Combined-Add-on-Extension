import bpy


def is_class_registered(cls):
    if hasattr(bpy.types, cls.__name__):
        print(f"Class {cls.__name__} is already registered")
        return True

    if not issubclass(cls, bpy.types.Operator) or not hasattr(cls, "bl_idname"):
        return False

    update_class_name = eval(f"bpy.ops.{cls.bl_idname}.idname()")
    print(f"update_class_name: {update_class_name}")

    return hasattr(bpy.types, update_class_name)


def create_scene_property(prop_name, prop_value):
    if hasattr(bpy.types.Scene, prop_name):
        return
    setattr(bpy.types.Scene, prop_name, prop_value)


def remove_scene_property(prop_name):
    if not hasattr(bpy.types.Scene, prop_name):
        return
    delattr(bpy.types.Scene, prop_name)
