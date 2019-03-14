import numpy as np
import matplotlib.pyplot as plt

#ndarray或者matrix去存储矩阵

#mat1 = np.array([[80,81],[82,83],[80,81],[82,83],[80,81],[82,83],[80,81],[82,83]])
#mat2 = np.mat([[80,81],[82,83],[80,81],[82,83],[80,81],[82,83],[80,81],[82,83]])
#print(mat1)
#print(mat2)

#矩阵乘法

matrix1=np.mat([[1,2],[3,4],[5,6]])
matrix2=np.mat([[1,2,3],[3,4,6]])
print(matrix2*matrix1)

#np.matmul,ndarray的乘法

#np.hsstack数组合并
#np.concatenate() 合并
a = np.array([80,81])
b = np.array([82,83])
print(np.hstack([a,b]))
print(np.concatenate([a,b]))
#np.arrange 分割
