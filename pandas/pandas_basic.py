import pandas as pd
import numpy as np

stock_change = np.random.normal(0,1,(10,5))


pd.DataFrame(stock_change)   #DataFrame 既有行索引又有列索引的二维数组
stock = ["股票{}".format(i) for i  in range (10) ]  #行名
date = pd.date_range(start = "20180101",periods = 5,freq = "B")  #列名
data = pd.DataFrame(stock_change,index = stock, columns= date)
#data.shape   # 10,5
#data.columms
data.head(5)  #头五行
data.tail(3)  #后三行


#multiindex
#panel 存储三维结构的容器
#pd.Panel()  准备弃用

#pd.Series  只有行索引
print(pd.Series(np.arange(10)))
