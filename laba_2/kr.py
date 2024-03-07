import math
from laba_2_extra import *


a = AbsoluteBordersNumber(3.85, 0.01)
b = AbsoluteBordersNumber(2.0435, 0.0004)
c = AbsoluteBordersNumber(962.6, 0.1)

ab = a*b
denum = c.functional(lambda x: x**(1/3), lambda x: 1/(x**(2/3)))
res = ab/denum
print(res)
