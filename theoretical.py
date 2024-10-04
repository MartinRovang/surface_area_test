
import numpy as np


def cone_surface_area(radius, height):
    # Calculate the slant height of the cone
    slant_height = np.sqrt(radius**2 + height**2)
    
    # Calculate the lateral surface area
    lateral_surface_area = np.pi * radius * slant_height
    
    return lateral_surface_area