import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector


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