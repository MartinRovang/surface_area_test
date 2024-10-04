
from skimage import measure
import numpy as np


def calculate_surface_area_skimage_mm2(segmentation_volume: np.ndarray, resolution: np.ndarray) -> float:
    """
    Calculate the surface area of a segmented lesion in cm².

    Parameters:
        segmentation_volume (np.ndarray): The 3D segmentation mask volume.
        resolution (np.ndarray): The resolution of each voxel in the volume (spacing between voxels).

    Returns:
        float: The surface area in cm².
    """

    # Check if any of the axes are of size 1 (indicating a 2D slice)
    is_2d = np.any([dim == 1 for dim in segmentation_volume.shape])
    if is_2d:
        # Pad the volume to make it 3D if it's 2D
        segmentation_volume = np.pad(segmentation_volume, ((0, 0), (0, 0), (0, 1)), mode='constant')

    # Generate the mesh using the marching cubes algorithm
    verts, faces, _, _ = measure.marching_cubes(segmentation_volume, level=None, spacing=resolution, method='lorensen')

    # Calculate the surface area of the mesh in mm²
    surface_area_mm2 = mesh_surface_area(verts, faces)

    return surface_area_mm2


def mesh_surface_area(verts: np.ndarray, faces: np.ndarray) -> float:
    """
    Calculate the surface area of a mesh defined by vertices and faces.

    Parameters:
        verts (np.ndarray): Array of vertices.
        faces (np.ndarray): Array of faces, with each face being a triplet of vertex indices.

    Returns:
        float: The total surface area of the mesh.
    """
    # Vertices of each triangle
    v0 = verts[faces[:, 0]]
    v1 = verts[faces[:, 1]]
    v2 = verts[faces[:, 2]]

    # Compute the cross product of vectors (v1 - v0) and (v2 - v0) for each triangle
    cross_product = np.cross(v1 - v0, v2 - v0)

    # Calculate the area of each triangle
    area = np.linalg.norm(cross_product, axis=1) / 2.0

    # Sum the areas of all triangles to get the total surface area
    surface_area = np.sum(area)

    return surface_area