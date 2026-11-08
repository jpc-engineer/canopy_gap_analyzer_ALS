# Step 1: Airborne Data Ingestion & Validation
- Successfully ingested the Airborne LiDAR (ALS) LAZ file. To optimize memory, we extracted the scaled X, Y, Z coordinates alongside the LAS classification codes, stacking them into a single 2D NumPy array. We then applied a random spatial mask to retain a representative sample of 2,000,000 points.

### Results
- The resulting Z values range from ~644m to ~775m. This confirms the data represents absolute terrain elevation above sea level, not height above ground. The inclusion of the classification column will allow us to separate ground returns (Class 2) from vegetation returns in the normalization step.

# Step 2: Ground Normalization (Height Above Ground)
- Airborne LiDAR captures absolute elevation (height above sea level). To accurately analyze forest structure, we must convert these elevations into Height Above Ground (HAG).
First separate the point cloud into ground returns (Class 2) and vegetation returns (Classes 3-5). Using a 2D scipy.spatial.KDTree built from the ground points' X and Y coordinates, we queried the nearest ground point for every vegetation point. By subtracting the nearest ground elevation from the vegetation elevation, we mathematically 'flatten' the terrain. The result is a normalized point cloud where Z=0 represents the forest floor, allowing for accurate vertical strata filtering in the next step.

### Results
- Using a KDTree, we successfully matched every vegetation point to its nearest ground point in the horizontal plane and subtracted the ground elevation.
- **Max height**: 60.5m (consistent with tall Australian rainforests)
- **Mean height**: 18.7m (Realistic average canopy height)
- **Min height**: -1.5m (Minor negative values are expected due to micro-terrain dips)
- The resulting veg_normalized.npy array now contains true Height above ground (HAG) values, ready for strata filtering.

# Step 3: Strata Filtering (Normalized Heights)
- Using the Height above ground normalized vegetation data, we applied vertical strata filtering.
  
### Results
- **Understory** (0-2m): 224,698 points (16.8%)
- **Midstory** (2-15m): 198,085 points (14.8%)
- **Canopy** (>15m): 914,865 points (64.8%)
- This distribution is consistent with a mature Australian forest, where the canopy layer dominates the point cloud, with substantial understory and midstory regeneration.
