import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix


# TEST 1
u = Matrix([
    [1., 0.],
    [0., 1.]
])

print("__ test 1 __\n")
print("u = Matrix([\n\
    [1., 0.],\n\
    [0., 1.]\n\
])")

r1 = u.trace()
print("\033[94m")
print("u.trace()")
print("->", r1)
print("<- 2.0")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [2., -5., 0.],
    [4., 3., 7.],
    [-2., 3., 4.]
])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [2., -5., 0.],\n\
    [4., 3., 7.],\n\
    [-2., 3., 4.]\n\
])")

r2 = u.trace()
print("\033[94m")
print("u.trace()")
print("->", r2)
print("<- 9.0")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [-2., -8., 4.],
    [1., -23., 4.],
    [0., 6., 4.]
])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [-2., -8., 4.],\n\
    [1., -23., 4.],\n\
    [0., 6., 4.]\n\
])")

r3 = u.trace()
print("\033[94m")
print("u.trace()")
print("->", r3)
print("<- -21.0")
print("\033[0m")