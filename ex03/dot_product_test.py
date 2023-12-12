import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector

u = Vector([0., 0.])
v = Vector([1., 1.])
print(u.dot(v))
# 0.0

u = Vector([1., 1.])
v = Vector([1., 1.])
print(u.dot(v))
# 2.0

u = Vector([-1., 6.])
v = Vector([3., 2.])
print(u.dot(v))
# 9.0