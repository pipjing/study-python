# coding:utf8
class Dog(object):
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age


    def sit(self):
        """模拟小狗被命令是蹲下"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """模拟小狗被命令式打滚"""
        print(self.name.title() + " rolled over")

my_dog = Dog('zhangjiaxin',22)
my_dog.sit()
my_dog.roll_over()