import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from classes.matrix import Matrix


u = Vector([2., 3.])
v = Vector([5., 7.])
u.add(v)
print(u)


u = Vector([2., 3.])
v = Vector([5., 7.])
u.sub(v)
print(u)


u = Vector([2., 3.])
u.scl(2.)
print(u)


u = Matrix([
    [1., 2.],
    [3., 4.]
])
v = Matrix([
    [7., 4.],
    [-2., 2.]
])
u.add(v)
print(u)


u = Matrix([
    [1., 2.],
    [3., 4.]
])
v = Matrix([
    [7., 4.],
    [-2., 2.]
])
u.sub(v)
print(u)


u = Matrix([
    [1., 2.],
    [3., 4.]
])
u.scl(2.)
print(u)