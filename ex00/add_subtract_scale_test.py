import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector


mul = Vector([1, 1.])
v = Vector([3., 6.])
v.add(mul)
print(v)