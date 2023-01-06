import open3d as o3d
import numpy as np
from tqdm import tqdm
import random

obj = o3d.io.read_point_cloud('object-global.pcd')
obj.colors = o3d.utility.Vector3dVector(np.zeros_like(obj.points) + [255, 0, 0])
scene = o3d.io.read_point_cloud('scene.pcd')

o3d.visualization.draw_geometries([obj, scene],
                                  window_name='Before global alignment')

tree = o3d.geometry.KDTreeSearchParamKNN(knn=10)
obj.estimate_normals(tree)
scene.estimate_normals(tree)

tree2 = o3d.geometry.KDTreeSearchParamRadius(0.05)
objFeatures = o3d.pipelines.registration.compute_fpfh_feature(obj, tree2)
sceneFeatures = o3d.pipelines.registration.compute_fpfh_feature(obj, tree2)

objFeatures = np.asarray(objFeatures.data).T
sceneFeatures = np.asarray(sceneFeatures.data).T

corr = o3d.utility.Vector2iVector()
for j in tqdm(range(objFeatures.shape[0]), desc='Correspondences'):
    fobj = objFeatures[j]
    dist = np.sum((fobj - sceneFeatures)**2, axis=-1)
    kmin = np.argmin(dist)
    corr.append((j, kmin))

tree3 = o3d.geometry.KDTreeFlann(scene)

iters = 100
threshSquared = 0.01 ** 2

random.seed(123456789)
inliersBest = 0
for i in tqdm(range(iters), desc='RANSAC'):
    corri = o3d.utility.Vector2iVector(random.choices(corr, k=3))
    est = o3d.pipelines.registration.TransformationEstimationPointToPoint()
    T = est.compute_transformation(obj, scene, corri)

    objAligned = o3d.geometry.PointCloud(obj)
    objAligned.transform(T)

    inliers = 0
    for j in range(len(objAligned.points)):
        k, idx, dist = tree3.search_knn_vector_3d(objAligned.points[j], 1)
        if dist[0] < threshSquared:
            inliers += 1

    if inliers > inliersBest:
        print(f'Got a new model with {inliers}/{len(objAligned.points)} inliers!')
        inliersBest = inliers
        pose = T

print('Got the following pose:')
print(pose)

o3d.visualization.draw_geometries([obj.transform(pose), scene],
                                  window_name='After global alignment')
