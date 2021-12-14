# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

class Employee:
    def __init__(self, name, tip):
        self.name = name
        self.tip = tip

if __name__ == "__main__":
    emp1 = Employee("Evan", 10000)
    emp2 = Employee("Jihoon", 10000)
    print(emp1.name, emp2.name)

'''
# 문제점: 
# 기본팁이 만원이라면, 새로운 Staff이 추가될 때마다, 
# 10000 값을 입력해야 하는 번거로움이 발생
'''
