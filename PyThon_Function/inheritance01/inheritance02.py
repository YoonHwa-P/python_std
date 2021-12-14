# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

class Employee:
    MAX_TIP = 10000
    DEFAULT_TIP  = 2000
    def __init__(self, name, tip=0):
        self.name = name
        if tip>= Employee.MAX_TIP:
            self.tip = Employee.MAX_TIP
        elif tip < 2000:
            self.tip = DEFAULT_TIP
        else:
            self.tip = tip


if __name__ == "__main__":
    emp1 = Employee("kim")
    print(emp1.tip)
    emp2 = Employee("Lee", 40000)
    print(emp2.tip)
    emp3 = Employee("Park", 1500)
    print(emp3.tip)
