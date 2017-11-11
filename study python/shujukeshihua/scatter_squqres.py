# coding:utf8

import matplotlib.pyplot as plt
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values = range(1,1001)

y_values = [x**2 for x in x_values]

# edgecolor删除点的轮廓,c='red'或者(0,0,0.8)改变颜色
# 使用颜色映射cmap=plt.cm.Blues
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=50)
# 设置标题，加上坐标轴标签
plt.title(u"中文显示标题加u",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

# 每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
# plt.savefig('squares.png',bbox_inches='tight)自动保存图片
plt.show()