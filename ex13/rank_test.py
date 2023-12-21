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

r1 = u.rank()
print("\033[94m")
print("u.rank()")
print("->", r1)
print("<- 3")
print("\033[0m\n")


# TEST 2
u = Matrix([
    [ 1., 2., 0., 0.],
    [ 2., 4., 0., 0.],
    [-1., 2., 1., 1.],
])

print("__ test 2 __\n")
print("u = Matrix([\n\
    [ 1., 2., 0., 0.],\n\
    [ 2., 4., 0., 0.],\n\
    [-1., 2., 1., 1.]\n\
])")

r2 = u.rank()
print("\033[94m")
print("u.rank()")
print("->", r2)
print("<- 2")
print("\033[0m\n")


# TEST 3
u = Matrix([
    [ 8., 5., -2.],
    [ 4., 7., 20.],
    [ 7., 6., 1.],
    [21., 18., 7.],
])

print("__ test 3 __\n")
print("u = Matrix([\n\
    [ 8., 5., -2.],\n\
    [ 4., 7., 20.],\n\
    [ 7., 6., 1.],\n\
    [21., 18., 7.]\n\
])")

r3 = u.rank()
print("\033[94m")
print("u.rank()")
print("->", r3)
print("<- 3")
print("\033[0m")