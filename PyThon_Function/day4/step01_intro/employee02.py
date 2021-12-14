# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
1. 기존 코드에서 set_name 메서드 추가
2. 이름 설정 후 프린트
'''

class Employee:

    # 파라미터 2개를 입력한다. self, new_name
    def set_name(self, new_name):
        self.name = new_name

if __name__ == "__main__":
    emp = Employee()
    emp.set_name("Evan")
    print(emp.name)

