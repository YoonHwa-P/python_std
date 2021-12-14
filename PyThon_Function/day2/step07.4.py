# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# 1. global x, nonlocal x, x 자유롭게 사용
# 2. 반드시 gloval x or nonlocal x 사용
# 3. 변수 = x 만, 100, 70, 30, 70 순서로 출력


x = 100

def a():
    x=70
    return print(x)
def b():
    global x
    x = 70
    return print(x)
def c():
    x=30
    return print(x)


if __name__ == "__main__":
    for function in [a, b, c]:
        print(function)
        function()
        print("---")
        print(x)