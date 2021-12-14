# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
1. 기존 코드에서 give_raise(), weekly_tip() 메서드 추가
'''

class Employee:

    # 파라미터 2개를 입력한다. self, new_name
    def set_name(self, name):
        self.name = name

    # 파라미터 2개를 입력한다. self, new_tip
    def set_tip(self, tip):
        self.tip = tip

    # give_raise() 추가
    def give_raise(self, new_tip):
        self.tip = self.tip + new_tip

    # weekly_tip() 추가
    def weekly_tip(self):
        return self.tip / 7

if __name__ == "__main__":
    emp = Employee()
    emp.set_name("Evan")
    print(emp.name)
    emp.set_tip(50000)
    print(emp.tip)
    emp.tip = emp.tip + 1500
    print(emp.tip)
    emp.give_raise(1500)
    print(emp.tip)
    weekly_tips = emp.weekly_tip()
    print(weekly_tips)


