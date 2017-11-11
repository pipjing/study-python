# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from  random_walk import RandomWalk

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

while True:
    rw = RandomWalk()
    rw.fill_walk()
    # 设置窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    # 重新着色起点和终点
    plt.scatter(rw.x_values, rw.y_values, c=rw.y_values,cmap=plt.cm.Blues, s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none', s=100)


    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_going = raw_input(u"大爷，是否继续？(y/n):")
    if keep_going == 'n':
        break

