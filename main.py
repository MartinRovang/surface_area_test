
import create_cone
import theoretical
import neomedsys
import pyrad

# Parameters for the cone
radius = 20
height = 50
grid_size = 100
resolution = [1, 1, 1]


# Create a cone using the create_cone module
cone = create_cone.create_cone(radius, height, grid_size, resolution)

# Calculate the surface area of the cone using the theoretical formula
theoretical_surface_area = theoretical.cone_surface_area(radius, height)

# Calculate the surface area of the cone using the neomedsys module
neomedsys_surface_area = neomedsys.calculate_surface_area_skimage_mm2(cone, resolution)

# Calculate the surface area of the cone using the pyrad module

pyrad_surface_area = pyrad.calculate_surface_area_pyrad(cone, resolution)

print(f"Theoretical surface area: {theoretical_surface_area} mm²")
print(f"NeoMedSys surface area: {neomedsys_surface_area} mm²")
print(f"Pyrad surface area: {pyrad_surface_area} mm²")
