# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
1. 기존 코드에서 set_tip 메서드 추가
2. 이번에는 tip 금액 입력 후, 추가
'''

class Employee:

    # 파라미터 2개를 입력한다. self, new_name
    def set_name(self, new_name):
        self.name = new_name

    # 파라미터 2개를 입력한다. self, new_tip
    def set_tip(self, new_tip):
        self.tip = new_tip

if __name__ == "__main__":
    emp = Employee()
    emp.set_name("Evan")
    emp.set_tip(5000)
    print(emp.name)
    print(emp.tip)

