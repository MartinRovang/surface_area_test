

import SimpleITK as sitk
import numpy as np

def calculate_surface_area_sitk(mask_path):
    # Read the image and mask
    mask = sitk.ReadImage(mask_path)

    # Create a LabelShapeStatisticsImageFilter
    label_shape_filter = sitk.LabelShapeStatisticsImageFilter()
    label_shape_filter.Execute(mask)

    # Get the surface area
    surface_area = label_shape_filter.GetPerimeter(1)  # 1 is the label we're interested in

    return surface_area
