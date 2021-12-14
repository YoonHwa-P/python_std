# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

def math_functions(func_name):
    """사칙연산을 하는 함수

    :param func_name:
    :return:
    """
    if func_name == "add":
        def add(a, b):
            return a+b
        return add
    elif func_name == "minus":
        def minus(a, b):
            return a-b
        return minus
    elif func_name == "mpc":
        def mpc(a, b):
            return a*b
        return mpc
    elif func_name == "dvs":
        def dvs(a, b):
            return a/b
        return dvs
    else:
        print("사칙 연산 만 할 수 있답니다.")


if __name__ == "__main__":
    x = 100
    y = 2

    add = math_functions("add")
    minus = math_functions("minus")
    mpc = math_functions("mpc")
    dvs = math_functions("dvs")

    # 사칙연산
    print("100 + 2 = {}".format(add(x,y)))
    print("100 - 2 = {}".format(minus(x,y)))
    print("100 * 2 = {}".format(mpc(x,y)))
    print("100 / 2 = {}".format(dvs(x,y)))