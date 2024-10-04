
import numpy as np


def cone_surface_area(radius, height):
    # Calculate the slant height of the cone
    slant_height = np.sqrt(radius**2 + height**2)
    
    # Calculate the lateral surface area
    lateral_surface_area = np.pi * radius * slant_height

    # Calculate the base area
    base_area = np.pi * radius**2

    # Calculate the total surface area
    total_surface_area = lateral_surface_area + base_area

    return total_surface_area