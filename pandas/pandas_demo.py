import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("c:\operation_log.csv")
#print(data.head())
#print(data.iloc[1,1])  #取某一个位置的值，也可用于赋值
#data.iloc(1,2)
#data.ix[:4,1]

#print(data.OperationTime)
#data.OperationTime = 1 #赋值
# print(data.sort_values(by = 'ClientIP',ascending=False)) # 排序
#print(data.describe())
#print(data["ClientIP"] + "a")
#function:add/sub = +/-

#按条件查询
#print(data[(data['LoginName'] == 'admin') & (data['ClientIP'] =='192.168.0.160')])
#print(data.query("LoginName == 'admin'"))
#print(data['LoginName'].isin(['admin']))

#统计
#data.describe()
#print(data['OperationTime'].max())

#idxmax and idxmin 最大值和最小值的位置
#print(data['OperationTime'].cumsum())
#data['OperationTime'].cumsum().plot()

#func:自定义函数


data2 = pd.read_csv("c:\modelcount.csv",delimiter="	",encoding="utf_8")   #usecols=('col1','clo2') 只读某些列，names列名
print(data2.head())
print(data2.shape)
#data2['counter'].cumsum().plot()
#data2.plot()
#plt.show()  #pycharm 必须
data2.to_csv("c:\\1.csv",encoding="utf_8_sig")