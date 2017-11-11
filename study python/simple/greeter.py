# coding:utf8
name = raw_input("请输入您的姓名:")
print 'hello!' + name + '!'

total = raw_input("请输入你想要的机器人数量：")
all_alien_number = int(total)
# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(all_alien_number):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens:
    print(alien)
print("...")

# 显示创建了多少外星人
print("外星人总数：" + str(len(aliens)))

