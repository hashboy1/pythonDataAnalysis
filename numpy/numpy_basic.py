import numpy as np
import matplotlib.pyplot as plt
score = np.array([[81,82,83,84,85],[85,82,83,86,85],[81,88,83,81,91],[81,80,83,84,82],[81,81,83,81,85]])
#基本属性
print(score)
print(score.shape)
print(score.ndim)
print(score.size)
print(score.dtype)

#0,1数组
zero = np.zeros([4,5])
print(zero)
ones = np.ones([4,5])
print(ones)

#改值取值
print(score[3,3])
score[3,3] = 10
print(score[3,3])

#随机数数组
line = np.linspace(0,10,5)   #5是几个
print(line)
range = np.arange(0,11,5)    #5是步长
print(range)

#均匀分布
uniform = np.random.uniform(-1,1,10000)
print(uniform)
plt.figure()
plt.hist(uniform,10)
plt.show()

#正态分布
normal= np.random.normal(1.75,0.1,10000)
print(normal)
plt.figure()
plt.hist(normal,1000)
plt.show()



stock_change = np.random.normal(0,1,[8,10])
#print(stock_change[0,0:3])
print(stock_change)
#print(stock_change.reshape(10,8))
stock_change.resize(10,8)
print(stock_change)
#ndarray.reshape返回新的，原始的不改
#ndarray.resize 原始数据修改


#三维数据
#stock3 = np.random.normal(0,1,[2,3,4])
#print(stock3)

#类型修改
print(stock_change.astype("int32"))
#ndarray 序列化
print(stock_change.tostring())

#去重
temp=np.array([[1,2,3,4],[4,3,5,6]])
print(np.unique(temp))