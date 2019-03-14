import matplotlib.pyplot as py
import random
x = range(50)
y_shanghai= [random.uniform(15,18) for i in x]
y_beijing= [random.uniform(1,10) for i in x]
py.figure()

py.scatter(x,y_shanghai,color='r',label="shanghai")  #散点
py.scatter(x,y_beijing,color='b',label="beijing")

#py.plot(x,y_shanghai,color='r',label="shanghai")   #折线
#py.plot(x,y_beijing,color='b',label="beijing")

#修改xy刻度
x_label = [ "11点{}分".format(i) for i in x]   #注意用{}
py.xticks(x[::5],x_label[::5])
py.yticks(range(0,40,5))

#comment
py.grid(True)
py.title("summary")
py.xlabel("x-scale")
py.ylabel("y-scale")
py.legend(loc="upper right")   #显示图例

py.show()
