# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

class Employee:
    def set_name(self, new_name):
        self.new_name = new_name


if __name__ == "__main__":
    emp = Employee()

    emp.set_name("YH")
    print(emp.new_name)
