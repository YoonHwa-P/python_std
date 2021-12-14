# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-

'''
- 클래스 메서드 사용
- 즉, 필수적으로 공통된 사용되는 메서드들을 사용한다는 뜻
'''

import os

class Employee:
    MIN_TIP = 1000

    def __init__(self, name, tip=1000):
        self.name = name

        if tip >= Employee.MIN_TIP:
            self.tip = tip
        else:
            self.tip = Employee.MIN_TIP

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.read()
        return cls(name)

if __name__ == "__main__":
    # create an employee without calling Employee()
    # emp = open('employee_data.txt')
    emp = Employee.from_file("sample_data/employee_data.txt")
    print(emp.name)
