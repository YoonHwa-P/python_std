# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-

class Employee:
    MIN_TIP = 30000

    def __init__(self, name, tip = MIN_TIP):
        self.name = name
        if tip >= Employee.MIN_TIP:
            self.tip = tip
        else:
            self.tip = Employee.MIN_TIP

    def give_raise(self, amount):
        self.tip += amount

# Define Child Class
class Manager(Employee):
    pass

if __name__ == "__main__":
    mng = Manager("Evan", 60000)
    print(mng.name)
    print(mng.tip)