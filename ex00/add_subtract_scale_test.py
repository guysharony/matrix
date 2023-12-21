import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from classes.matrix import Matrix

# TEST 1
u = Vector([2., 3.])
v = Vector([5., 7.])
print("__ test 1 __\n")
print("u = Vector([2., 3.])")
print("v = Vector([5., 7.])")

u.add(v)
print("\033[94m")
print("u.add(v)")
print("->", u)
print("<- [7.0, 10.0]")
print("\033[0m\n")


# TEST 2
u = Vector([2., 3.])
v = Vector([5., 7.])
print("__ test 2 __\n")
print("u = Vector([2., 3.])")
print("v = Vector([5., 7.])")

u.sub(v)
print("\033[94m")
print("u.sub(v)")
print("->", u)
print("<- [-3.0, -4.0]")
print("\033[0m\n")


# TEST 3
u = Vector([2., 3.])
print("__ test 3 __\n")
print("u = Vector([2., 3.])")

u.scl(2.)
print("\033[94m")
print("u.scl(2.)")
print("->", u)
print("<- [4.0, 6.0]")
print("\033[0m\n")


# TEST 4
u = Matrix([
    [1., 2.],
    [3., 4.]
])
v = Matrix([
    [7., 4.],
    [-2., 2.]
])
print("__ test 4 __\n")
print("u = Matrix([\n\
    [1., 2.],\n\
    [3., 4.]\n\
])")
print("v = Matrix([\n\
    [7., 4.],\n\
    [-2., 2.]\n\
])")

u.add(v)
print("\033[94m")
print("u.add(v)")
print("->", u)
print("<- [[8.0, 6.0], [1.0, 6.0]]")
print("\033[0m\n")


# TEST 5
u = Matrix([
    [1., 2.],
    [3., 4.]
])
v = Matrix([
    [7., 4.],
    [-2., 2.]
])
print("__ test 5 __\n")
print("u = Matrix([\n\
    [1., 2.],\n\
    [3., 4.]\n\
])")
print("v = Matrix([\n\
    [7., 4.],\n\
    [-2., 2.]\n\
])")

u.sub(v)
print("\033[94m")
print("u.sub(v)")
print("->", u)
print("<- [[-6.0, -2.0], [5.0, 2.0]]")
print("\033[0m\n")


# TEST 6
u = Matrix([
    [1., 2.],
    [3., 4.]
])
print("__ test 6 __\n")
print("u = Matrix([\n\
    [1., 2.],\n\
    [3., 4.]\n\
])")

u.scl(2.)
print("\033[94m")
print("u.scl(2.)")
print("->", u)
print("<- [[2.0, 4.0], [6.0, 8.0]]")
print("\033[0m")