import laspy
import numpy as np
import pyvista as pv

# Load data
las = laspy.read("data/bonangStateForest.laz")

# Extract scaled coordinates and classifications
x = las.x
y = las.y
z = las.z
classifications = np.array(las.classification)


# Combine into a single 2D array
all_data = np.column_stack((x, y, z, classifications))
print(all_data.shape)

# Subset for memory
point_limit = 2000000
random_indices = np.random.choice(all_data.shape[0], point_limit, replace=False)

# Apply mask to combined array
points_matrix = all_data[random_indices]

# Save to file
np.save("raw_coords.npy", points_matrix)

print(f"Saved {points_matrix.shape[0]} points with {points_matrix.shape[1]} features.")
print(f"First 5 points (X, Y, Z, Classification):\n", points_matrix[:5])

# Quick viz
#cl = pv.PolyData(las.xyz)
#cl.plot(render_points_as_spheres=True, point_size=6)
