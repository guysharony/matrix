import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix

u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
])
print(u.rank())
# 3

u = Matrix([
    [ 1., 2., 0., 0.],
    [ 2., 4., 0., 0.],
    [-1., 2., 1., 1.],
])
print(u.rank())
# 2

u = Matrix([
    [ 8., 5., -2.],
    [ 4., 7., 20.],
    [ 7., 6., 1.],
    [21., 18., 7.],
])
print(u.rank())
# 3