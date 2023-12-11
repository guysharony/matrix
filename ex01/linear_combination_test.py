import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex01.linear_combination import linear_combination


e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])

v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])

print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
# [10.]
# [-2.]
# [0.5]
print(linear_combination([v1, v2], [10., -2.]))
# [10.]
# [0.]
# [230.]