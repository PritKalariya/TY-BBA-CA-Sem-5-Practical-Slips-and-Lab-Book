# Write python script using package to calculate area and volume of cube and sphere

from myPackage import Cube
from myPackage import Sphere


cube = Cube(10)
print(cube.get_area())

sphere = Sphere(10)
print(sphere.get_area())