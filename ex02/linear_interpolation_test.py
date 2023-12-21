import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix
from classes.vector import Vector
from ex02.linear_interpolation import lerp

# TEST 1
print("__ test 1 __")
r1 = lerp(0., 1., 0.)
print("\033[94m")
print("lerp(0., 1., 0.)")
print("->", r1)
print("<- 0.0")
print("\033[0m\n")


# TEST 2
print("__ test 2 __")
r2 = lerp(0., 1., 1.)
print("\033[94m")
print("lerp(0., 1., 1.)")
print("->", r2)
print("<- 1.0")
print("\033[0m\n")


# TEST 3
print("__ test 3 __")
r3 = lerp(0., 1., 0.5)
print("\033[94m")
print("lerp(0., 1., 0.5)")
print("->", r3)
print("<- 0.5")
print("\033[0m\n")


# TEST 4
print("__ test 4 __")
r4 = lerp(21., 42., 0.3)
print("\033[94m")
print("lerp(21., 42., 0.3)")
print("->", r4)
print("<- 27.3")
print("\033[0m\n")


# TEST 5
print("__ test 5 __")
r5 = lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)
print("\033[94m")
print("lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)")
print("->", r5)
print("<- [2.6, 1.3]")
print("\033[0m\n")


# TEST 6
print("__ test 6 __")
r6 = lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5)
print("\033[94m")
print("lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5)")
print("->", r6)
print("<- [[11.0, 5.5], [16.5, 22.0]]")
print("\033[0m")