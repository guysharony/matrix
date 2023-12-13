import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.vector import Vector
from ex06.cross_product import cross_product


u = Vector([0., 0., 1.])
v = Vector([1., 0., 0.])
print(cross_product(u, v))
# [0.]
# [1.]
# [0.]

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(cross_product(u, v))
# [-3.]
# [6.]
# [-3.]

u = Vector([4., 2., -3.])
v = Vector([-2., -5., 16.])
print(cross_product(u, v))
# [17.]
# [-58.]
# [-16.]