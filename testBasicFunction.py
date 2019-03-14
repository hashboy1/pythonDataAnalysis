import random
import math

x = range(30)
y = [random.uniform(15,18) for i in x]
print(y)
l = 10
z = ["{}+{}".format(i,l) for i in x]
print(z)

f = [math.sin(i) for i in x]
print(f)
print(x[::5])


d = [math.sin(i) for i in x]
print(f)


