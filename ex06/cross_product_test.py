import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex06.cross_product import cross_product


# TEST 1
u = Vector([0., 0., 1.])
v = Vector([1., 0., 0.])

print("__ test 1 __\n")
print("u = Vector([0., 0., 1.])")
print("v = Vector([1., 0., 0.])")

r1 = cross_product(u, v)
print("\033[94m")
print("cross_product(u, v)")
print("->", r1)
print("<- [0.0, 1.0, 0.0]")
print("\033[0m\n")


# TEST 2
u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])

print("__ test 2 __\n")
print("u = Vector([1., 2., 3.])")
print("v = Vector([4., 5., 6.])")

r2 = cross_product(u, v)
print("\033[94m")
print("cross_product(u, v)")
print("->", r2)
print("<- [-3.0, 6.0, -3.0]")
print("\033[0m\n")


# TEST 3
u = Vector([4., 2., -3.])
v = Vector([-2., -5., 16.])

print("__ test 3 __\n")
print("u = Vector([4., 2., -3.])")
print("v = Vector([-2., -5., 16.])")

r3 = cross_product(u, v)
print("\033[94m")
print("cross_product(u, v)")
print("->", r3)
print("<- [17.0, -58.0, -16.0]")
print("\033[0m")