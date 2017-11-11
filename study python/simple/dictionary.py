# coding:utf8
# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens:
    print(alien)
print("...")

# 显示创建了多少外星人
print("外星人总数：" + str(len(aliens)))

# 修改前3个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[:5]:
    print '修改后外星人前五个',alien