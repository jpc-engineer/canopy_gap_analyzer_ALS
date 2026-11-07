## Step 1: Data ingestion

- I first load the raw LiDAR data so I can inspect and prepare the 3D coordinates for spatial math. I specifically need the X, Y and Z coordinate arrays to be extracted from the compressed LAZ file and returned as structured NumPy arrays, so I can move on to filtering these points into ecological layers, understory/canopy etc.

### Step 1 results
- To optimize memory usage for local development, I extracted the scaled X, Y, Z coordinates and applied a random spatial mask to limit sample to 1,000,000 points. 
- The resulting coordinates confirm a local Terrestrial LiDAR coordinate system, with the scanner near the origin (0,0,0). X,Y,Z values represent radial distance from the scanner (-764 to +53m), and Z values represent realistic canopy heights up to 74 metres.
   
## Step 2: Strata Filtering

- To analyze canopy gaps I have to first isolate relevant forest layers. I applied NumPy boolean masking to the Z-axis (height) of the dataset to extract three distinct ecological strata:
- **Understory** (0m - 2m) 36947 points (ground level vegetation)
- **Midstory** (2m > 15m) 178,268 points (mid level vegetation)
- **Canopy** (> 15m) 730,581 points (the overhead tree cover)
  

