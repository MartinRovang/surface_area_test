
import create_cone
import theoretical
import neomedsys
import pyrad
from rich import print
from rich.console import Console
from rich.table import Table

# Parameters for the cone
radius = 20
height = 100
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

# the differences in %
diff_neomedsys = (theoretical_surface_area - neomedsys_surface_area) / theoretical_surface_area * 100
diff_pyrad = (theoretical_surface_area - pyrad_surface_area) / theoretical_surface_area * 100


# Create a console instance
console = Console()

# Create a table
table = Table(title="Surface Area Comparison")

# Add columns
table.add_column(f"r={radius}, h={height}, grid={grid_size}", justify="right", style="cyan")
table.add_column("Surface Area (mm²)", justify="right", style="magenta")
table.add_column("Error (%)", justify="right", style="yellow")

# Add rows with data
table.add_row("Theoretical Surface Area", f"{theoretical_surface_area:.2f}", "")
table.add_row("NeoMedSys Surface Area", f"{neomedsys_surface_area:.2f}", f"{diff_neomedsys:.2f}")
table.add_row("Pyrad Surface Area", f"{pyrad_surface_area:.2f}", f"{diff_pyrad:.2f}")

# Print the table
console.print(table)