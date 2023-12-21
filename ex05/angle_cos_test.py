import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex05.angle_cos import angle_cos

# TEST 1
u = Vector([1., 0.])
v = Vector([1., 0.])

print("__ test 1 __\n")
print("u = Vector([1., 0.])")
print("v = Vector([1., 0.])")

r1 = angle_cos(u, v)
print("\033[94m")
print("angle_cos(u, v)")
print("->", r1)
print("<- 1.0")
print("\033[0m\n")


# TEST 2
u = Vector([1., 0.])
v = Vector([0., 1.])

print("__ test 2 __\n")
print("u = Vector([1., 0.])")
print("v = Vector([0., 1.])")

r2 = angle_cos(u, v)
print("\033[94m")
print("angle_cos(u, v)")
print("->", r2)
print("<- 0.0")
print("\033[0m\n")


# TEST 3
u = Vector([-1., 1.])
v = Vector([ 1., -1.])

print("__ test 3 __\n")
print("u = Vector([-1., 1.])")
print("v = Vector([ 1., -1.])")

r3 = angle_cos(u, v)
print("\033[94m")
print("angle_cos(u, v)")
print("->", r3)
print("<- -1.0")
print("\033[0m\n")


# TEST 4
u = Vector([2., 1.])
v = Vector([4., 2.])

print("__ test 4 __\n")
print("u = Vector([2., 1.])")
print("v = Vector([4., 2.])")

r4 = angle_cos(u, v)
print("\033[94m")
print("angle_cos(u, v)")
print("->", r4)
print("<- 1.0")
print("\033[0m\n")


# TEST 5
u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])

print("__ test 5 __\n")
print("u = Vector([1., 2., 3.])")
print("v = Vector([4., 5., 6.])")

r5 = angle_cos(u, v)
print("\033[94m")
print("angle_cos(u, v)")
print("->", r5)
print("<- 0.974631846")
print("\033[0m")