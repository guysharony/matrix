import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from classes.matrix import Matrix


# TEST 1
u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = Vector([4., 2.])

print("__ test 1 __\n")
print("u = Matrix([\n\
    [1., 0.],\n\
    [0., 1.]\n\
])")
print("v = Vector([4., 2.])")

r1 = u.mul_vec(v)
print("\033[94m")
print("u.mul_vec(v)")
print("->", r1)
print("<- [4.0, 2.0]")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [2., 0.],
    [0., 2.]
])
v = Vector([4., 2.])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [2., 0.],\n\
    [0., 2.]\n\
])")
print("v = Vector([4., 2.])")

r2 = u.mul_vec(v)
print("\033[94m")
print("u.mul_vec(v)")
print("->", r2)
print("<- [8.0, 4.0]")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [2., -2.],
    [-2., 2.]
])
v = Vector([4., 2.])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [2., -2.],\n\
    [-2., 2.]\n\
])")
print("v = Vector([4., 2.])")

r3 = u.mul_vec(v)
print("\033[94m")
print("u.mul_vec(v)")
print("->", r3)
print("<- [4.0, -4.0]")
print("\033[0m\n")


# TEST 4
u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = Matrix([
    [1., 0.],
    [0., 1.]
])

print("__ test 4 __\n")
print("u = Matrix([\n\
    [1., 0.],\n\
    [0., 1.]\n\
])")
print("v = Matrix([\n\
    [1., 0.],\n\
    [0., 1.]\n\
])")

r4 = u.mul_mat(v)
print("\033[94m")
print("u.mul_mat(v)")
print("->", r4)
print("<- [[1.0, 0.0], [0.0, 1.0]]")
print("\033[0m\n")


# TEST 5
u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = Matrix([
    [2., 1.],
    [4., 2.]
])

print("__ test 5 __\n")
print("u = Matrix([\n\
    [1., 0.],\n\
    [0., 1.]\n\
])")
print("v = Matrix([\n\
    [2., 1.],\n\
    [4., 2.]\n\
])")

r5 = u.mul_mat(v)
print("\033[94m")
print("u.mul_mat(v)")
print("->", r5)
print("<- [[2.0, 1.0], [4.0, 2.0]]")
print("\033[0m\n")


# TEST 6
u = Matrix([
    [3., -5.],
    [6., 8.]
])
v = Matrix([
    [2., 1.],
    [4., 2.]
])

print("__ test 6 __\n")
print("u = Matrix([\n\
    [3., -5.],\n\
    [6., 8.]\n\
])")
print("v = Matrix([\n\
    [2., 1.],\n\
    [4., 2.]\n\
])")

r6 = u.mul_mat(v)
print("\033[94m")
print("u.mul_mat(v)")
print("->", r6)
print("<- [[-14.0, -7.0], [44.0, 22.0]]")
print("\033[0m")