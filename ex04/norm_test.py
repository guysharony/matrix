import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector


# TEST 1
u = Vector([0., 0., 0.])

print("__ test 1 __\n")
print("u = Vector([0., 0., 0.])")

r1_norm_1, r1_norm, r1_norm_inf = u.norm_1(), u.norm(), u.norm_inf()
print("\033[94m")
print("u.norm_1(), u.norm(), u.norm_inf()")
print("->", r1_norm_1, r1_norm, r1_norm_inf)
print("<- 0.0 0.0 0.0")
print("\033[0m\n")


# TEST 2
u = Vector([1., 2., 3.])

print("__ test 2 __\n")
print("u = Vector([1., 2., 3.])")

r2_norm_1, r2_norm, r2_norm_inf = u.norm_1(), u.norm(), u.norm_inf()
print("\033[94m")
print("u.norm_1(), u.norm(), u.norm_inf()")
print("->", r2_norm_1, r2_norm, r2_norm_inf)
print("<- 6.0 3.74165738 3.0")
print("\033[0m\n")


# TEST 3
u = Vector([-1., -2.])

print("__ test 3 __\n")
print("u = Vector([-1., -2.])")

r3_norm_1, r3_norm, r3_norm_inf = u.norm_1(), u.norm(), u.norm_inf()
print("\033[94m")
print("u.norm_1(), u.norm(), u.norm_inf()")
print("->", r3_norm_1, r3_norm, r3_norm_inf)
print("<- 3.0 2.236067977 2.0")
print("\033[0m")