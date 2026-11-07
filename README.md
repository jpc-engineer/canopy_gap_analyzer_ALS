# Step 1: Airborne Data Ingestion & Validation
- Successfully ingested the Airborne LiDAR (ALS) LAZ file. To optimize memory, we extracted the scaled X, Y, Z coordinates alongside the LAS classification codes, stacking them into a single 2D NumPy array. We then applied a random spatial mask to retain a representative sample of 2,000,000 points.
  
Validation Check: The resulting Z values range from ~644m to ~775m. This confirms the data represents absolute terrain elevation above sea level, not height above ground. The inclusion of the classification column will allow us to separate ground returns (Class 2) from vegetation returns in the normalization step.
