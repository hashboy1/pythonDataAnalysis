import numpy as np
import random
import time
python_list = []
for i in range(100000000):
    python_list.append(random.random())
ndarray_list = np.array(python_list)
#sumary by trandition python
t1 = time.time()
a=sum(python_list)
t2 = time.time()
print(a)
print(t2-t1)

#sumary by ndarray
t1 = time.time()
a=np.sum(ndarray_list)
t2 = time.time()
print(a)
print(t2-t1)