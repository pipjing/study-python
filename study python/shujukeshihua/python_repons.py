# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)


response_dict = r.json()

print u'项目总数:',response_dict['total_count']

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print u'仓库总数：',len(repo_dicts)

# 研究第一个仓库
repo_dict = repo_dicts[0]
print "\nKeys:", len(repo_dict)
for key in sorted(repo_dict.keys()):
    print key




print(response_dict.keys())