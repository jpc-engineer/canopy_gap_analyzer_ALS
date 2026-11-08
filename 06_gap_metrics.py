import numpy as np
from scipy.spatial import ConvexHull

# Load gap points
gap_pts = np.load("data/gap_boundary_points.npy")

gaps_xy = gap_pts[:, 0:2]

# calculate gap area
hull = ConvexHull(gaps_xy)
gap_area_m2 = hull.area

print(f"Total Gap Boundary Points: {len(gap_pts)}")
print(f"Calculated Gap Area: {gap_area_m2:.2f} m²")

# calculate bounding box area to compute gap coverage percentage
veg = np.load("data/veg_normalized.npy")
x_min, x_max = np.min(veg[:, 0]), np.max(veg[:, 0])
y_min, y_max = np.min(veg[:, 1]), np.max(veg[:, 1])

# calculate width, length to get total area m2
plot_width = x_max - x_min
plot_length = y_max - y_min
total_area_m2 = plot_width * plot_length

gap_coverage_pct = (gap_area_m2 / total_area_m2) * 100
print(f"Total Plot Area: {total_area_m2:,.2f} m² ({total_area_m2/10000:.2f} hectares)")
print(f"Gap Coverage: {gap_coverage_pct:.2f}%")
