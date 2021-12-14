# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : UTF-8

class SalaryExcept(ValueError): pass # 상속
class TipExept(SalaryExcept): pass # 상속

class Employee:

    MIN_SALARY = 30000
    MAX_Bonus = 20000

    def __init__(self, name, salary = 30000):
        self.name = name
        if salary< Employee.MIN_SALARY:
            raise SalaryExcept("급여가 너무 낮아요!")
        self.salary = salary

    def give_bonus(self, amount):
        if amount > Employee.MAX_Bonus:
            print("보너스가 너무 많아 ")
        elif self.salary + amount < Employee.MIN_SALARY :
            print("보너스 지급 후의 급여도 매우 낮다. ")
        else:
            self.salary += amount

if __name__ == "__main__":
    emp = Employee("YH", salary= 10000)

    try:
        emp.give_bonus(70000)
    except SalaryExcept:
        print("Error Salary")

    try:
        emp.give_bonus(-10000)
    except tipExcept:
        print("Error Tip")