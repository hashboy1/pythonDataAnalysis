import matplotlib.pyplot as py
import random
x = range(50)
y_shanghai= [random.uniform(15,18) for i in x]
y_beijing= [random.uniform(1,10) for i in x]


figure,axes = py.subplots(nrows = 1,ncols=2 )


axes[0].plot(x,y_shanghai,color='r',label="shanghai")
axes[1].plot(x,y_beijing,color='b',label="beijing")

#修改xy刻度
x_label = [ "11点{}分".format(i) for i in x]   #注意用{}
axes[0].set_xticks(x[::5],x_label[::5])
axes[0].set_yticks(range(0,40,5))
axes[1].set_xticks(x[::5],x_label[::5])
axes[1].set_yticks(range(0,40,5))

#comment
axes[0].grid(True)
axes[0].set_title("summary")
axes[0].set_xlabel("x-scale")
axes[0].set_ylabel("y-scale")
axes[0].legend(loc="upper right")   #显示图例
axes[1].grid(True)
axes[1].set_title("summary")
axes[1].set_xlabel("x-scale")
axes[1].set_ylabel("y-scale")
axes[1].legend(loc="upper right")   #显示图例

py.show()
