import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex05.angle_cos import angle_cos

u = Vector([1., 0.])
v = Vector([1., 0.])
print(angle_cos(u, v))
# 1.0

u = Vector([1., 0.])
v = Vector([0., 1.])
print(angle_cos(u, v))
# 0.0

u = Vector([-1., 1.])
v = Vector([ 1., -1.])
print(angle_cos(u, v))
# -1.0

u = Vector([2., 1.])
v = Vector([4., 2.])
print(angle_cos(u, v))
# 1.0

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(angle_cos(u, v))
# 0.974631846