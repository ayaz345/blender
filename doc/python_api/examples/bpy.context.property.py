"""
Get the property associated with a hovered button.
Returns a tuple of the datablock, data path to the property, and array index.
"""


if active_property := bpy.context.property:
    datablock, data_path, index = active_property
    datablock.keyframe_insert(data_path=data_path, index=index, frame=1)
