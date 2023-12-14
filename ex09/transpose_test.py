import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.matrix import Matrix

u = Matrix([
    [1., 0.],
    [0., 1.]
])
print(u.transpose())
# [1., 0.],
# [0., 1.]

u = Matrix([
    [2., -5., 0.],
    [4., 3., 7.]
])
print(u.transpose())
# [2. , 4.],
# [-5., 3.],
# [0. , 7.],

u = Matrix([
    [-2., -8.],
    [1., -23.],
    [0., 6.]
])
print(u.transpose())
# [-2.,   1., 0.],
# [-8., -23., 6.]