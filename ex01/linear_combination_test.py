import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex01.linear_combination import linear_combination


# TEST 1
e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])

print("__ test 1 __\n")
print("e1 = Vector([1., 0., 0.])")
print("e2 = Vector([0., 1., 0.])")
print("e3 = Vector([0., 0., 1.])")
print("\033[94m")

r1 = linear_combination([e1, e2, e3], [10., -2., 0.5])
print("linear_combination([e1, e2, e3], [10., -2., 0.5])")
print("->", r1)
print("<- [10.0, -2.0, 0.5]")
print("\033[0m\n")

# TEST 2
v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])

print("__ test 2 __\n")
print("v1 = Vector([1., 2., 3.])")
print("v2 = Vector([0., 10., -100.])")

r2 = linear_combination([v1, v2], [10., -2.])
print("\033[94m")
print("linear_combination([v1, v2], [10., -2.])")
print("->", r2)
print("<- [10.0, 0.0, 230.0]")
print("\033[0m")