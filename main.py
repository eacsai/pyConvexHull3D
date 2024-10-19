from hull3D import ConvexHull3D
import numpy as np

import mpl_toolkits.mplot3d as mpl3D
import matplotlib.pyplot as plt

np.random.seed(20)
# pts = np.random.randint(-100, 100, (50,3))
# 读取文件并解析点数据
def read_points_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            # 去除换行符并按空格分割每行数据
            coords = line.strip().split()
            # 将字符串转换为浮点数或整数，并添加到列表中
            point = [float(coord) for coord in coords]
            points.append(point)
    
    # 将列表转换为numpy数组，方便后续操作
    return np.array(points)

# 假设文件名为 'points.dot'
file_path = 'points.dot'
points = read_points_from_file(file_path)


# Showing default parameters
Hull = ConvexHull3D(points, run=True, make_frames=True, frames_dir='./frames/')

# To get Vertex objects:
# vertices = Hull.DCEL.vertexDict.values()

# To get indices:
pts = Hull.pts   # to get pts in order used by ConvexHull3d
vertices = []
in_points = []
for i, pt in enumerate(pts):
    if i in Hull.getVertexIndices():
        vertices.append(pt)
    else:
        in_points.append(pt)
vertices = np.array(vertices)
in_points = np.array(in_points)
fig = plt.figure(figsize=[20, 15])  # 创建图形窗口
ax = fig.add_subplot(111, projection='3d')  # 在图形窗口中添加三维坐标轴
ax.set_xlim([Hull.boxmin,Hull.boxmax])
ax.set_ylim([Hull.boxmin,Hull.boxmax])
ax.set_zlim([Hull.boxmin,Hull.boxmax])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], s=50, c='r', marker='o')
ax.scatter(in_points[:,0], in_points[:,1], in_points[:,2], s=50, c='r', marker='o', alpha=0.3)

for face in Hull.DCEL.faceDict.values():
    tri = mpl3D.art3d.Poly3DCollection([[list(v.p()) for v in face.loopOuterVertices()]])
    tri.set_facecolor((0,0,1, 0.2)) # add functionality for visible faces later
    #tri.set_alpha(0.1)
    tri.set_edgecolor((0,0,0, 0.2))
    ax.add_collection3d(tri)

plt.savefig('result.png')
plt.close()
# To get vertices of each Face:
# faces = [[list(v.p()) for v in face.loopOuterVertices()] for face in Hull.faceDict.values()]