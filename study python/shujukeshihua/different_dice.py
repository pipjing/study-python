# coding:utf8
import pygal
import matplotlib.pyplot as plt

from die import Die
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(2000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化
hist = pygal.Bar()

hist.title = u"两个butong骰子一千次随机测试结果"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = u"事件"
hist.y_title = u"频率"

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual3.svg')



print(frequencies)