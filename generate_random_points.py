# adds 100 points with random coordinates (within 2-units cube)

import bpy, bmesh, random

bpy.ops.object.add(type='MESH')
bpy.context.active_object.name = 'Points Cloud'
bm = bmesh.new()

for i in range(0, 100):
    bmesh.ops.create_vert(bm, co=[(random.random()*2 - 1), (random.random()*2 - 1), (random.random()*2 - 1)])
    
bm.to_mesh(bpy.context.active_object.data)
bm.free()