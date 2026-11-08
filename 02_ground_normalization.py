import numpy as np
from scipy.spatial import KDTree

# Load data
points = np.load("data/raw_coords.npy")

# Separate earth from the trees
ground_mask = points[:, 3] == 2
veg_mask = points[:, 3] != 2

ground_pts = points[ground_mask]
veg_pts = points[veg_mask]

# We only care about ground directly below the tree, so pass the X,Y ground_pts coordinates to the KDTree 
tree = KDTree(ground_pts[:, 0:2])

# Query tree using X,Y veg_pts coordinates
distances, indices = tree.query(veg_pts[:, 0:2])

# Calculate height above ground
nearest_ground_z = ground_pts[indices, 2]
normalized_z = veg_pts[:, 2] - nearest_ground_z

print(f"MAX: {np.max(normalized_z)}.. MIN: {np.min(normalized_z)}... MEAN: {np.mean(normalized_z)}")

# update Z column in veg_points array with new normalized_z
veg_pts[:, 2] = normalized_z

# Normalize ground points to Z = 0 for clean visual floor
ground_normalized = ground_pts.copy()
ground_normalized[:, 2] = 0.0

# Save
np.save("data/veg_normalized.npy", veg_pts)
np.save("data/ground_normalized.npy", ground_normalized)

print(f"Vegetation shape: {veg_pts.shape}")
print(f"Ground shape: {ground_normalized.shape}")

