# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-


# rull 2_ nested function : 중첩함수
def a():
    """
    List가 담긴 함수 a
    :return:
    """
    x = [3, 6, 9]

    def b(y):
        print(y)

    for value in x: # leng = 3
        print("value :", value)
        b(x)

if __name__ == "__main__":
    print(a())

#
