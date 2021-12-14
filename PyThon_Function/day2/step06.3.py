# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

def my_func():
    return 10

def docstring_exist(func):
    """ 입력된 함수 내에 docstring이 존재 하는지 확인하는 함수
    :args
        func (callable) : A function

    :return
        bool
    """
    return func.__doc__ is not None # T or F

def no_docstring():
    return 10

def yes_docstring():
    """value 반환하는 함수
    :return:
    """
    return 10

if __name__ == "__main__":
    x = my_func
    print(x())
    print("------")
    print(docstring_exist(no_docstring))
    print(docstring_exist(yes_docstring))
