# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

class Employee:
    def set_name(self, new_name):
        self.new_name = new_name

    def set_tip(self, tip):
        self.tip = tip

    def give_raise(self, new_tip):
        self.tip = self.tip + new_tip

    def weekly_tip(self):
        return self.tip /7

if __name__ == "__main__":
    emp = Employee()

    emp.set_name("YH")
    print(emp.new_name)

    emp.set_tip(9000)
    print(emp.tip)

    emp.give_raise(1500)
    print(emp.tip)

    weekly_tip = emp.weekly_tip(emp.tip)
    print(weekly_tip)