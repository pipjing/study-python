# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

xs = range(1,100)
y = [x*x for x in xs]
plt.plot(xs,y,linewidth=5)

# 设置标题，加上坐标轴标签
plt.title(u"中文显示标题加u",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()