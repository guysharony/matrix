import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector

# TEST 1
u = Vector([0., 0.])
v = Vector([1., 1.])

print("__ test 1 __\n")
print("u = Vector([0., 0.])")
print("v = Vector([1., 1.])")

r1 = u.dot(v)
print("\033[94m")
print("u.dot(v)")
print("->", r1)
print("<- 0.0")
print("\033[0m\n")


# TEST 2
u = Vector([1., 1.])
v = Vector([1., 1.])

print("__ test 2 __\n")
print("u = Vector([1., 1.])")
print("v = Vector([1., 1.])")

r2 = u.dot(v)
print("\033[94m")
print("u.dot(v)")
print("->", r2)
print("<- 2.0")
print("\033[0m\n")


# TEST 3
u = Vector([-1., 6.])
v = Vector([3., 2.])

print("__ test 3 __\n")
print("u = Vector([-1., 6.])")
print("v = Vector([3., 2.])")

r3 = u.dot(v)
print("\033[94m")
print("u.dot(v)")
print("->", r3)
print("<- 9.0")
print("\033[0m")