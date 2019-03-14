import matplotlib.pyplot as py
import random
import math
x = range(50)
y= [math.ceil(i) for i in x]

py.figure()
py.plot(x,y)
py.show()
