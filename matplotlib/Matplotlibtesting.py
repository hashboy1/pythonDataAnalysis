import matplotlib.pyplot as py
#py.figure(figsize=(100,100),dpi=50)  #画布size和清晰度
py.figure()
py.plot([1,2,3,4,5,6,7],[7,6,5,7,3,2,7])
py.savefig("a.png")   #必须在show之前
py.show()
