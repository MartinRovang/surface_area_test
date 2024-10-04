

import numpy as np
import nibabel as nib


def create_cone(radius, height, grid_size, resolution=[1, 1, 1]):
    # Create a grid of the specified size
    cone = np.zeros((grid_size, grid_size, height), dtype=np.uint8)

    # Define the center of the cone's base
    center_x, center_y = grid_size // 2, grid_size // 2

    # Iterate over the grid to populate the cone
    for z in range(height):
        for x in range(grid_size):
            for y in range(grid_size):
                # Distance from the center at the current height level
                dist_from_center = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

                # Calculate the current allowable radius for the given height (linearly decreasing)
                max_radius_at_z = (1 - z / height) * radius

                # Mark the voxel as part of the cone if it's within the radius
                if dist_from_center <= max_radius_at_z:
                    cone[x, y, z] = 1

    # save the binary cone as a NIfTI image
    affine = np.eye(4)
    affine[0, 0] = resolution[0]
    affine[1, 1] = resolution[1]
    affine[2, 2] = resolution[2]

    nifti_image = nib.Nifti1Image(cone, affine)
    nib.save(nifti_image, 'binary_cone.nii.gz')

    return cone
