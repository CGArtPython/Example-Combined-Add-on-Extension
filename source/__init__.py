import bpy

from bpy.types import Panel

from . import add_on_node_arrange
from . import utils

class NAP_PT_NodePanel(Panel):
    bl_label = "Node Arrange Plus"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Arrange"

    def draw(self, context):
        if context.active_node is None:
            return

        layout = self.layout

        row = layout.row()
        row.operator('node.duplicate', text="Duplicate (Node Arrange Plus)")

        row = layout.row()
        row.operator('node.button')

        row = layout.row()
        row.prop(bpy.context.scene, 'nodemargin_x', text="Margin x")
        row = layout.row()
        row.prop(bpy.context.scene, 'nodemargin_y', text="Margin y")
        row = layout.row()
        row.prop(context.scene, 'node_center', text="Center nodes")

        row = layout.row()
        row.operator('node.na_align_nodes', text="Align to Selected")

        row = layout.row()
        node = context.space_data.node_tree.nodes.active
        if node and node.select:
            row.prop(node, 'location', text = "Node X", index = 0)
            row.prop(node, 'location', text = "Node Y", index = 1)
            row = layout.row()
            row.prop(node, 'width', text = "Node width")

        row = layout.row()
        row.operator('node.button_odd')


classes = [
    NAP_PT_NodePanel,
    add_on_node_arrange.NA_OT_NodeButton,
    add_on_node_arrange.NA_OT_NodeButtonOdd,
    add_on_node_arrange.NA_OT_NodeButtonCenter,
    add_on_node_arrange.NA_OT_ArrangeNodesOp,
    add_on_node_arrange.NA_OT_AlignNodes
]


properties = [
    ('nodemargin_x', bpy.props.IntProperty(default=100, update=add_on_node_arrange.nodemargin)),
    ('nodemargin_y', bpy.props.IntProperty(default=20, update=add_on_node_arrange.nodemargin)),
    ('node_center', bpy.props.BoolProperty(default=True, update=add_on_node_arrange.nodemargin))
]


def register():
    print(f"Registering {__name__}")
    for c in classes:
        if utils.is_class_registered(c):
            print(f"\tClass {c.__name__} is already registered")
            continue
        print(f"\tRegistering class {c.__name__}")
        bpy.utils.register_class(c)

    for prop in properties:
        print(f"\tRegistering property {prop[0]})")
        utils.create_scene_property(*prop)


def unregister():
    for c in classes:
        if not utils.is_class_registered(c):
            print(f"\tClass {c.__name__} is not registered")
            continue
        print(f"\tUnregistering class {c.__name__}")
        bpy.utils.unregister_class(c)

    for prop in properties:
        utils.remove_scene_property(prop[0])


if __name__ == "__main__":
    register()
