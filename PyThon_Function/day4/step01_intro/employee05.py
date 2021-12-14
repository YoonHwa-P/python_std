# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
# init constructor 추가
## 예제
- 좋은 예제들 1: https://andamiro25.tistory.com/38
- 좋은 예제들 2: https://realpython.com/python3-object-oriented-programming/
'''

class Employee:

    # init constructor
    def __init__(self, name, tip = 0):
        # 이름과 tip 변수 정의
        self.name = name
        self.tip = tip

    def give_raise(self, amount):
        self.tip += amount

    def weekly_tip(self):
        return self.tip / 7

if __name__ == "__main__":
    emp = Employee("Evan", 50000)
    print(emp.name)
    print(emp.tip)
    emp.tip = emp.tip + 1500
    print(emp.tip)
    emp.give_raise(1500)
    print(emp.tip)
    weekly_tips = emp.weekly_tip()
    print(weekly_tips)