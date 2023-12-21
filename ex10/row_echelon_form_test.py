import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix

# TEST 1
u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.]
])

print("__ test 1 __\n")
print("u = Matrix([\n\
    [1., 0., 0.],\n\
    [0., 1., 0.],\n\
    [0., 0., 1.]\n\
])")

r1 = u.row_echelon()
print("\033[94m")
print("u.row_echelon()")
print("->", r1)
print("<- [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [1., 2.],
    [3., 4.]
])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [1., 2.],\n\
    [3., 4.]\n\
])")

r2 = u.row_echelon()
print("\033[94m")
print("u.row_echelon()")
print("->", r2)
print("<- [[1.0, 0.0], [0.0, 1.0]]")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [1., 2.],
    [2., 4.]
])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [1., 2.],\n\
    [2., 4.]\n\
])")

r3 = u.row_echelon()
print("\033[94m")
print("u.row_echelon()")
print("->", r3)
print("<- [[1.0, 2.0], [0.0, 0.0]]")
print("\033[0m\n")


# TEST 4
u = Matrix([
    [8., 5., -2., 4., 28.],
    [4., 2.5, 20., 4., -4.],
    [8., 5., 1., 4., 17.]
])

print("__ test 4 __\n")
print("u = Matrix([\n\
    [8., 5., -2., 4., 28.],\n\
    [4., 2.5, 20., 4., -4.],\n\
    [8., 5., 1., 4., 17.]\n\
])")

r4 = u.row_echelon()
print("\033[94m")
print("u.row_echelon()")
print("->", r4)
print("<- [[1.0, 0.625, 0.0, 0.0, -12.1666667], [0.0, 0.0, 1.0, 0.0, -3.6666667], [0.0, 0.0, 0.0, 1.0, 29.5]]")
print("\033[0m")