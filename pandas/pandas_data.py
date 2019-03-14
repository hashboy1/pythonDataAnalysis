import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data = pd.read_csv("c:\operation_log.csv")
#print(pd.isnull(data))  #是否存在缺失值
#print(np.any(pd.isnull(data)))  #是否存在缺失值
#print(data.dropna())  #删除缺失值
#print(data.fillna('Nothing'))  #缺失值处理
#data["OperationTime"].mean() #平均值


path="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
dataAdult = pd.read_csv(path,names=["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country"])
print(dataAdult)
#print(dataAdult.replace(to_replace=" ?",value="unknown"))


#数据离散化
#sr = pd.cut(data,[])
#pd.getdummies(sr)
#合并
#pd.concat
#pd.merge

#交叉表
#pd.crosstab(data1,data2)
#分组与聚合