# coding:utf8
class Car(object):
    """一次模拟car的简单尝试"""

    def __init__(self,make,model,year):
        """初始化car属性"""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """秒速性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

my_car = Car('audi', 'a4',2016)
print(my_car.get_descriptive_name())