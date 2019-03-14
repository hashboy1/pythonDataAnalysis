import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql

conn=pymysql.connect(host='192.168.0.160',user='3dms',password='vrkb',database='3dmsv2',charset='utf8mb4')
cur=conn.cursor()
cur.execute("select model_id,model_name,type_id from model_master")
row=cur.fetchall()
#print(type(row))
#print((row))
model_master=pd.DataFrame(list(row),columns=["model_id","model_name","type_id"])
#print(model_master)

cur.execute("select model_type_id,model_type_name from model_type")
row2=cur.fetchall()
model_type=pd.DataFrame(list(row2),columns=["type_id","model_type_name"])
#print(model_type)

summary=pd.merge(model_master,model_type,how='inner',on=['type_id','type_id'])

#print(summary)
#print(summary["model_id"].sum())
#print(summary.query("type_id" == "7"))
#print(summary[( summary['type_id'] == 7 )])    #条件查询

count=summary[( summary['type_id'] == 7 )].count()
#print(count)
#print(count[3])   #series取值
#print(summary.iloc[3,1])  #定点取值


#print(summary.groupby('model_type_name').groups)
group_by_name=summary.groupby('model_type_name')   #分组
print(group_by_name.get_group('交通工具1'))          #分组查询

conn.close()