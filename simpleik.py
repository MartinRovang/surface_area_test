

import SimpleITK as sitk
import numpy as np

def calculate_surface_area_sitk(segmentation_volume, resolution):
    # Read the image and mask
    segmentation_volume = sitk.GetImageFromArray(np.transpose(segmentation_volume))
    segmentation_volume.SetSpacing(resolution)
    # Create a LabelShapeStatisticsImageFilter
    label_shape_filter = sitk.LabelShapeStatisticsImageFilter()
    label_shape_filter.Execute(segmentation_volume)

    # Get the surface area
    surface_area = label_shape_filter.GetPerimeter(1)  # 1 is the label we're interested in

    return surface_area
