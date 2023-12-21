import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix


# TEST 1
u = Matrix([
    [ 1., -1.],
    [-1., 1.]
])

print("__ test 1 __\n")
print("u = Matrix([\n\
    [1., -1.],\n\
    [-1., 1.]\n\
])")

r1 = u.determinant()
print("\033[94m")
print("u.determinant()")
print("->", r1)
print("<- 0.0")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [2., 0., 0.],
    [0., 2., 0.],
    [0., 0., 2.]
])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [2., 0., 0.],\n\
    [0., 2., 0.],\n\
    [0., 0., 2.]\n\
])")

r2 = u.determinant()
print("\033[94m")
print("u.determinant()")
print("->", r2)
print("<- 8.0")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [8., 5., -2.],
    [4., 7., 20.],
    [7., 6., 1.]
])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [8., 5., -2.],\n\
    [4., 7., 20.],\n\
    [7., 6., 1.]\n\
])")

r3 = u.determinant()
print("\033[94m")
print("u.determinant()")
print("->", r3)
print("<- -174.0")
print("\033[0m\n")


# TEST 4
u = Matrix([
    [ 8., 5., -2., 4.],
    [ 4., 2.5, 20., 4.],
    [ 8., 5., 1., 4.],
    [28., -4., 17., 1.]
])

print("__ test 4 __\n")
print("u = Matrix([\n\
    [8., 5., -2., 4.],\n\
    [4., 2.5, 20., 4.],\n\
    [8., 5., 1., 4.],\n\
    [28., -4., 17., 1.]\n\
])")

r4 = u.determinant()
print("\033[94m")
print("u.determinant()")
print("->", r4)
print("<- 1032.0")
print("\033[0m")