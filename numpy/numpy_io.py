import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("c:\\Gas.csv",delimiter=";")
#字符串会解析为nan(float类型)
print(data)
data[np.isnan(data)] = 2
print(data)
#这方法不推荐，推荐用pandas