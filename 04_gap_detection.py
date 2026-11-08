import numpy as np
from scipy.spatial import KDTree

# For every understory point, is there a any canopy point within a 4 meter horizontal radius directly above me?
# if yes: understory point in under a closed canopy
# if no: understory point is under a canopy gap

understory_pts = np.load("data/understory.npy")
canopy_pts = np.load("data/canopy.npy")

understory_xy = understory_pts[:, 0:2]
canopy_xy = canopy_pts[:, 0:2]

tree = KDTree(canopy_xy)
neighbour_indices = tree.query_ball_point(understory_xy, r=4.0)

gap_mask = np.array([len(indices) == 0 for indices in neighbour_indices])
gaps = understory_pts[gap_mask]

print(f"Found {np.sum(gap_mask)} understory points located in gaps")

np.save("data/gap_boundary_points.npy", gaps)
print(f"Saved {gaps.shape[0]} gap boundary points with {gaps.shape[1]} features")
