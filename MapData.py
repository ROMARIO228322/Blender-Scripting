import bpy

# Hardcoded file path
file_path = 'C:\\M5221.asc'

# Read ASC file and extract height data
with open(file_path, 'r') as file:
    lines = file.readlines()

# Assuming data starts from line 7
height_data = [list(map(float, line.split())) for line in lines[6:]]

# Create a mesh based on height data
vertices = []
faces = []

for i in range(len(height_data)):
    for j in range(len(height_data[0])):
        vertices.append((i, j, height_data[i][j]))

for i in range(len(height_data) - 1):
    for j in range(len(height_data[0]) - 1):
        v1 = i * len(height_data[0]) + j
        v2 = v1 + 1
        v3 = v1 + len(height_data[0])
        v4 = v3 + 1
        faces.append((v1, v2, v4, v3))

mesh = bpy.data.meshes.new(name="HeightMapMesh")
mesh.from_pydata(vertices, [], faces)
mesh.update()

obj = bpy.data.objects.new("HeightMapObject", mesh)
bpy.context.scene.collection.objects.link(obj)