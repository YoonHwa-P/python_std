# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
- Class Attributes 사용이유
- 고정값인 최솟값 또는 최댓값이 필요할 때 사용
- `pi`와 같이 고정값이 관례적으로 지정된 경우 사용
'''

class Employee:
    MIN_TIP = 10000
    def __init__(self, name, tip=0):
        self.name = name

        if tip >= Employee.MIN_TIP:
            self.tip = tip
        else:
            self.tip = Employee.MIN_TIP

if __name__ == "__main__":
    emp0 = Employee("Default")
    print(emp0.tip)
    emp1 = Employee("Evan", 40000)
    print(emp1.tip)
