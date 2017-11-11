# coding:utf8
import json
import pygal
import matplotlib.pyplot as plt
import pygal.maps.world
from country_codes import get_country_code
from pygal.style import RotateStyle,LightColorizedStyle

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家的人口数量2010
# 创建一个包含人数的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population


# 根据人口数量进行分组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop <100000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

worldmap_chart = pygal.maps.world.World()

# 设置样式
worldmap_chart_style = RotateStyle('#336699',base_style=LightColorizedStyle)
worldmap_chart = pygal.maps.world.World(style=worldmap_chart_style)

worldmap_chart.title = u'2010年人口分布'
worldmap_chart.add('0-10m', cc_pops_1)
worldmap_chart.add('10m-1bn', cc_pops_2)
worldmap_chart.add('>1bn', cc_pops_3)



worldmap_chart.render_to_file('wpopulation.svg')