import open3d as o3d
import numpy as np
from tqdm import tqdm

obj = o3d.io.read_point_cloud('object-local.pcd')
obj.colors = o3d.utility.Vector3dVector(np.zeros_like(obj.points) + [255, 0, 0])
scene = o3d.io.read_point_cloud('scene.pcd')

o3d.visualization.draw_geometries([obj, scene],
                                  window_name='Before local alignment')
tree = o3d.geometry.KDTreeFlann(scene)

iters = 50
threshSquared = 0.01 ** 2
pose = None
objAligned = o3d.geometry.PointCloud(obj)
for i in tqdm(range(iters), desc='ICP'):
    corr = o3d.utility.Vector2iVector()
    for j in range(len(objAligned.points)):
        k, idx, dist = tree.search_knn_vector_3d(objAligned.points[j], 1)
        if dist[0] < threshSquared:
            corr.append((j, idx[0]))

    est = o3d.pipelines.registration.TransformationEstimationPointToPoint()
    T = est.compute_transformation(objAligned, scene, corr)
    objAligned.transform(T)
    pose = T if pose is None else T @ pose

print('Got the following pose:')
print(pose)

o3d.visualization.draw_geometries([obj.transform(pose), scene],
                                  window_name='After local alignment')
