# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# 함수를 객체로 저장해서 사용 할 수 있다.
# nested function
# nonlocal
# Closure : 상태값을 임시 저장 하기 위해
# --> decorator 함수를 배운다.

x= 100

def a(x) :
    def b():
        print(x)
    return b

if __name__ == "__main__":
    func = a(x)
    print(func())

    del(x) #100삭제
    print("*************************")
    print(type(func.__closure__)) # x=100을 삭제 했는데도 closure에 물려있어서 계속 나오게 된다.
    print(len(func.__closure__))
    print("closure:", func.__closure__[0].cell_contents)