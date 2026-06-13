import math

# Calculate the mass of the Earth.
# radius_Earth = 6356.91 # km
density_Earth = 5.52 # ton/m^3
radius_Earth = float(input("Enter the radius of the Earth: (km)"))
mass_Earth = (4/3)*math.pi*(radius_Earth*1000)**3*density_Earth
print("The mass of the Earth is %5.3e. "%(mass_Earth))
