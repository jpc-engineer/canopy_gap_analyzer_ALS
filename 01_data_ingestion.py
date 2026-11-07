import laspy
import numpy as np

las = laspy.read("data/bonangStateForest.laz")

coords = las.xyz
classifications = np.array(las.classification)
x = las.x
y = las.y
z = las.z

points = np.vstack([x, y, z, classifications])

point_limit = 2000000

random_indices = np.random.choice(coords.shape[0], point_limit, replace=False)

points_matrix = coords[random_indices]

np.save("raw_coords.npy", points_matrix)

print(f"Saved {points_matrix.shape[0]} points")
print(f"First 5 points (X, Y, Z):\n", points_matrix[:5])
