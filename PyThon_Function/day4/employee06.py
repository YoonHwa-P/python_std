# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

class Employee:
    # instance state == attribute
    def __init__(self, name, tip = 0):
        self.name = name
        self.tip = tip
        #tip이 음수가 들어가면 안됨.
        if tip < 0 :
            print("팁 금액은 양수여야 합니다. 다시 입력 ")

    def set_tip(self, tip):
        self.tip = tip

    def give_raise(self, new_tip):
        self.tip = self.tip + new_tip

    def weekly_tips(self):
        return self.tip /7

if __name__ == "__main__":
    emp = Employee("YH", -50000)

    print(emp.name)
    print(emp.tip)

    emp.tip = emp.tip + 1500
    print(emp.tip)

    emp.give_raise(1500)
    print(emp.tip)

    weekly_tips = emp.weekly_tips()
    print(weekly_tips)