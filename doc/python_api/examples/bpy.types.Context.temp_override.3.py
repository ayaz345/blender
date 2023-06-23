"""
This example shows how it's possible to add an object to the scene in another window.
"""

import bpy
from bpy import context

win_active = context.window
win_other = next(
    (
        win_iter
        for win_iter in context.window_manager.windows
        if win_iter != win_active
    ),
    None,
)
# Add cube in the other window.
with context.temp_override(window=win_other):
    bpy.ops.mesh.primitive_cube_add()
