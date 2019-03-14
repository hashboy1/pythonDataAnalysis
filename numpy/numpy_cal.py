import numpy as np
import matplotlib.pyplot as plt
stock_change = np.random.normal(0,1,[8,10])
stock_change = stock_change[0:5,0:5]
#print(stock_change)
#统一判断ndarray
#print(stock_change>0.5)
#条件返回
#print(stock_change[stock_change>0.5])
#条件赋值
#stock_change[stock_change>0.5] = 1
#print(stock_change)

#通用判断函数np.all and np.any
#所有符合
#print(np.all(stock_change>0))
#至少有一个符合
#print(np.any(stock_change>0))

#三元运算,为nparray赋值
#print(np.where(stock_change>0,1,0))
#print(np.logical_and(stock_change>0,stock_change<0.5))
#print(np.where(np.logical_and(stock_change>0,stock_change<0.5),1,0))

#统计运算
#print(np.max(stock_change))
#print(np.max(stock_change,axis=1))  #按列取最大值
#np.argmax 最大值所在位置


#数组与数组运算
#必须符合广播机制才能运算，纬度相等或形状（其中对应的一个地方为1）

arr1= np.array([[0,1,2],[4,5,6]])
arr2= np.array([[7,8,9],[10,11,12]])
print(arr1+1)
print(arr1*arr2)