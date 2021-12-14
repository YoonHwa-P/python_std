# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

'''
# init constructor 추가
## 예제
- 좋은 예제들 1: https://andamiro25.tistory.com/38
- 좋은 예제들 2: https://realpython.com/python3-object-oriented-programming/

# if_else
- tip이 음수가 될 때 별도로 처리 진행
'''

class Employee:

    # init constructor
    def __init__(self, name, tip = 0):
        # 이름과 tip 변수 정의
        self.name = name

        # 조건문 추가
        if tip >= 0:
            self.tip = tip
        else:
            self.tip = 0
            print("팁 금액은 0원이 될 수 없습니다. 다시 입력하시기를 바랍니다.")

    def give_raise(self, amount):
        self.tip += amount

    def weekly_tip(self):
        return self.tip / 7

if __name__ == "__main__":
    emp = Employee("Evan", -50000)
    print(emp.name)
    print(emp.tip)
    emp.tip = emp.tip + 1500
    print(emp.tip)
    emp.give_raise(1500)
    print(emp.tip)
    weekly_tips = emp.weekly_tip()
    print(weekly_tips)