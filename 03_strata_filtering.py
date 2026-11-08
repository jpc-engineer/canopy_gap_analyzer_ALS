import numpy as np
import pyvista as pv

veg_pts = np.load("data/veg_normalized.npy")

understory_mask = (veg_pts[:, 2] >= 0) & (veg_pts[:, 2] <= 2)
understory_pts = veg_pts[understory_mask]
print(len(understory_pts))

midstory_mask = (veg_pts[:, 2] > 2) & (veg_pts[:, 2] <= 15)
midstory_pts = veg_pts[midstory_mask]
print(len(midstory_pts))

canopy_mask = (veg_pts[:, 2] > 15)
canopy_pts = veg_pts[canopy_mask]
print(len(canopy_pts))

np.save("data/understory.npy", understory_pts)
np.save("data/midstory.npy", midstory_pts)
np.save("data/canopy.npy", canopy_pts)
