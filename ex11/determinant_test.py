import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix

u = Matrix([
    [ 1., -1.],
    [-1., 1.]
])
print(u.determinant())
# 0.0

u = Matrix([
    [2., 0., 0.],
    [0., 2., 0.],
    [0., 0., 2.]
])
print(u.determinant())
# 8.0

u = Matrix([
    [8., 5., -2.],
    [4., 7., 20.],
    [7., 6., 1.]
])
print(u.determinant())
# -174.0

u = Matrix([
    [ 8., 5., -2., 4.],
    [ 4., 2.5, 20., 4.],
    [ 8., 5., 1., 4.],
    [28., -4., 17., 1.]
])
print(u.determinant())
# 1032