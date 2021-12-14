# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-
# https://realpython.com/inheritance-composition-python/
# Inheritance and Composition: A Python OOP Guide

class Employee:
    def __init__(self, name, tip=30000):
        self.name = name
        self.tip = tip

    def give_raise(self, amount):
        self.tip += amount
        return self.tip

class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, tip=50000, project=None):
        Employee.__init__(self, name, tip)
        self.project = project

    # give_raise 메서드 추가
    def give_raise(self, amount = 0, bonus = 1.05):
        if amount > 0:
            Employee.give_raise(self, amount * bonus)
        else:
            Employee.give_raise(self, amount)

if __name__ == "__main__":
    mng = Manager("Evan")
    print(mng.name)
    print(mng.tip)
    mng.give_raise(2000, bonus=1.03)
    print(mng.tip)