import pyvista as pv
import numpy as np

def load_pc_mesh(file_path):
    try:
        points = np.load(file_path)
        if points.shape[1] != 3:
            raise ValueError(
                f"Expected shape (N, 3) for {file_path}, got {points.shape}."
            )
        mesh = pv.PolyData(points)
        return mesh
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found.")
        return None
    
def main():
    plotter = pv.Plotter()
    plotter.background_color = "white"

    ground = np.load("data/ground_normalized.npy")[:, 0:3]
    understory = np.load("data/understory.npy")[:, 0:3]
    midstory = np.load("data/midstory.npy")[:, 0:3]
    canopy = np.load("data/canopy.npy")[:, 0:3]
    gap_boundary = np.load("data/gap_boundary_points.npy")[:, 0:3]

    if ground is not None:
        plotter.add_mesh(
            pv.PolyData(ground),
            color="#A8A29E",
            point_size=2.0,
            render_points_as_spheres=True,
            name="Ground",
        )
    
    if understory is not None:
        plotter.add_mesh(
            pv.PolyData(understory),
            color="#90EE90",
            point_size=3.0,
            render_points_as_spheres=True,
            name="Understory",
        )

    if midstory is not None:
        plotter.add_mesh(
            pv.PolyData(midstory),
            color="#3CB371",
            point_size=3.5,
            render_points_as_spheres=True,
            name="Midstory",
        )

    if canopy is not None:
        plotter.add_mesh(
            pv.PolyData(canopy),
            color="#228B22",
            point_size=4.0,
            render_points_as_spheres=True,
            name="Canopy",
        )

    if gap_boundary is not None:
        plotter.add_mesh(
            pv.PolyData(gap_boundary),
            color="#FF0000",
            point_size=6.0,
            render_points_as_spheres=True,
            name="Gap Boundaries",
        )

    plotter.add_axes()

    print("Opening interactive 3D window...")
    plotter.show()

if __name__ == "__main__":
    main()


