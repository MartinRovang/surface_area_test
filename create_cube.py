
import numpy as np
import nibabel as nib


def create_cube(side_length, grid_size, resolution=[1, 1, 1]):
    # Create a grid of the specified size
    cube = np.zeros((grid_size, grid_size, grid_size), dtype=np.uint8)

    # Define the center of the cube
    center = grid_size // 2

    # Iterate over the grid to populate the cube
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                # Distance from the center in each dimension
                dist_from_center = np.abs(x - center), np.abs(y - center), np.abs(z - center)

                # Mark the voxel as part of the cube if it's within the side length
                if all(dist <= side_length / 2 for dist in dist_from_center):
                    cube[x, y, z] = 1

    # save the binary cube as a NIfTI image
    affine = np.eye(4)
    affine[0, 0] = resolution[0]
    affine[1, 1] = resolution[1]
    affine[2, 2] = resolution[2]

    nifti_image = nib.Nifti1Image(cube, affine)
    nib.save(nifti_image, 'binary_cube.nii.gz')

    return cube
