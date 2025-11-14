from stl import mesh
import numpy as np

length = 170
width = 120
thickness = 3

v = np.array([
    [0,0,0],
    [length,0,0],
    [length,width,0],
    [0,width
    h,0],
    [0,0,thickness],
    [length,0,thickness],
    [length,width,thickness],
    [0,width,thickness],
])

f = np.array([
    [0,1,2],[0,2,3],
    [4,5,6],[4,6,7],
    [0,1,5],[0,5,4],
    [1,2,6],[1,6,5],
    [2,3,7],[2,7,6],
    [3,0,4],[3,4,7]
])

m = mesh.Mesh(np.zeros(f.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(f):
    m.vectors[i] = v[face]

m.save("robot_deck.stl")
print("STL ready!")