# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# 데코레이터
# rull 1 : 함수를 객체로 사용하는 방식
# - 변수처리


def my_func():
    print("hello")

if __name__ == "__main__":
    x = my_func
    print(type(x))
    print(x())

    print_function = print
    print(print_function("파이썬이 재미 있다"))


# 다양한 함수를 리스트 안에 넣기
# 딕셔너리에 추가한다.

def my_func1():
    print("hello")

if __name__ == "__main__":
    list_function = [my_func1(), open, print]
    list_function[2]("전 리스트 안에 있어요 ")

    dict_fuctions = {
        "func_1": my_func1(),
        "func_2": open,
        "func_3": print,
    }
    print(dict_fuctions["func_3"]("이번에는 dictionary에 있다."))

# 결론 : 함수를 객체화 할 수 있따. 따라서 리스트와 딕셔너리로 사용 할 수 있다.
