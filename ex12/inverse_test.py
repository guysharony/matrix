import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix

# TEST 1
u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
])

print("__ test 1 __\n")
print("u = Matrix([\n\
    [1., 0., 0.],\n\
    [0., 1., 0.],\n\
    [0., 0., 1.]\n\
])")

r1 = u.inverse()
print("\033[94m")
print("u.inverse()")
print("->", r1)
print("<- [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [2., 0., 0.],
    [0., 2., 0.],
    [0., 0., 2.],
])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [2., 0., 0.],\n\
    [0., 2., 0.],\n\
    [0., 0., 2.]\n\
])")

r2 = u.inverse()
print("\033[94m")
print("u.inverse()")
print("->", r2)
print("<- [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [8., 5., -2.],
    [4., 7., 20.],
    [7., 6., 1.],
])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [8., 5., -2.],\n\
    [4., 7., 20.],\n\
    [7., 6., 1.]\n\
])")

r3 = u.inverse()
print("\033[94m")
print("u.inverse()")
print("->", r3)
print("<- [[0.649425287, 0.097701149, -0.655172414], [-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]]")
print("\033[0m")