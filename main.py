
import create_cone
import create_cube
import theoretical
import neomedsys
import pyrad
from rich import print
from rich.console import Console
from rich.table import Table

# Parameters for the cone
radius = 50
height = 30
grid_size = 100
resolution = [1, 1, 1]

side_length = 50

# Create a cone using the create_cone module
cone = create_cone.create_cone(radius, height, grid_size, resolution)
cube = create_cube.create_cube(side_length, grid_size, resolution)

# Calculate the surface area of the cone using the theoretical formula
theoretical_surface_area_cone = theoretical.cone_surface_area(radius, height)
theoretical_surface_area_cube = theoretical.cube_surface_area(side_length)

# Calculate the surface area of the cone using the neomedsys module
neomedsys_surface_area_cone = neomedsys.calculate_surface_area_skimage_mm2(cone, resolution)
neomedsys_surface_area_cube = neomedsys.calculate_surface_area_skimage_mm2(cube, resolution)

# Calculate the surface area of the cone using the pyrad module

pyrad_surface_area_cone = pyrad.calculate_surface_area_pyrad(cone, resolution)
pyrad_surface_area_cube = pyrad.calculate_surface_area_pyrad(cube, resolution)


# the differences in %
diff_neomedsys_cone = (theoretical_surface_area_cone - neomedsys_surface_area_cone) / theoretical_surface_area_cone * 100
diff_pyrad_cone = (theoretical_surface_area_cone - pyrad_surface_area_cone) / theoretical_surface_area_cone * 100

diff_neomedsys_cube = (theoretical_surface_area_cube - neomedsys_surface_area_cube) / theoretical_surface_area_cube * 100
diff_pyrad_cube = (theoretical_surface_area_cube - pyrad_surface_area_cube) / theoretical_surface_area_cube * 100

# Create a console instance
console = Console()

# Create a table
table = Table(title="Surface Area Comparison")

# Add columns
table.add_column(f"*Cone* r={radius}, h={height}, grid={grid_size}", justify="right", style="cyan")
table.add_column("Surface Area (mm²)", justify="right", style="magenta")
table.add_column("Error (%)", justify="right", style="red")

# Add rows with data
table.add_row("Theoretical Surface Area", f"{theoretical_surface_area_cone:.2f}", "")
table.add_row("NeoMedSys Surface Area", f"{neomedsys_surface_area_cone:.2f}", f"{diff_neomedsys_cone:.2f}")
table.add_row("Pyrad Surface Area", f"{pyrad_surface_area_cone:.2f}", f"{diff_pyrad_cone:.2f}")

# Print the table
console.print(table)

# Create a table
table = Table(title="Surface Area Comparison")

# Add columns
table.add_column(f"*Cube* side={side_length}, grid={grid_size}", justify="right", style="cyan")
table.add_column("Surface Area (mm²)", justify="right", style="magenta")
table.add_column("Error (%)", justify="right", style="red")

# Add rows with data
table.add_row("Theoretical Surface Area", f"{theoretical_surface_area_cube:.2f}", "")
table.add_row("NeoMedSys Surface Area", f"{neomedsys_surface_area_cube:.2f}", f"{diff_neomedsys_cube:.2f}")
table.add_row("Pyrad Surface Area", f"{pyrad_surface_area_cube:.2f}", f"{diff_pyrad_cube:.2f}")

# Print the table
console.print(table)

