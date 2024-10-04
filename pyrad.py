from radiomics import featureextractor
import numpy as np
import SimpleITK as sitk


def calculate_surface_area_pyrad(segmentation_volume: np.ndarray, resolution: np.ndarray) -> float:
    """
    Calculate the surface area of a segmented lesion in cm² using Pyradiomics.

    Parameters:
        segmentation_volume (np.ndarray): The 3D segmentation mask volume.
        resolution (np.ndarray): The resolution of each voxel in the volume (spacing between voxels).

    Returns:
        float: The surface area in cm².
    """
    # Initialize the Pyradiomics feature extractor
    extractor = featureextractor.RadiomicsFeatureExtractor()
    # Disable all features
    extractor.disableAllFeatures()
    # Enable the original_shape_SurfaceArea feature
    extractor.enableFeatureClassByName('shape')

    # make sikt object
    segmentation_volume = sitk.GetImageFromArray(np.transpose(segmentation_volume))
    segmentation_volume.SetSpacing(resolution)

    # Extract features from the NIfTI image
    results = extractor.execute(segmentation_volume, segmentation_volume)

    # Get the surface area feature value
    surface_area = results['original_shape_SurfaceArea']

    return surface_area
