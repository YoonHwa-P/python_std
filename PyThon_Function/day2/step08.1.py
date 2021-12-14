# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# 함수를 객체로 저장해서 사용 할 수 있다. 
# nested function
# nonlocal
# Closure : 상태값을 임시 저장 하기 위해
# --> decorator 함수를 배운다.

def a() :
    a =123
    def b():
        print(a)
    return b

if __name__ == "__main__":
    func = a()
    func()
    print("*************************")
    print(type(func.__closure__))
    print(len(func.__closure__))
    print(func.__closure__[0].cell_contents)