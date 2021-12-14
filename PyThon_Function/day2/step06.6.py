# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# Nested function 활용 예

def a(x, y):
    """

    :param x: Num
    :param y: Num
    :return:
    """
    def within_range(z):
        return z>5 and z<8

    if within_range(x) and within_range(y) :
        print(x * y)
    else:
        print("please enter other number")
        raise ValueError("X is {}, y is {}".format(x, y))

if __name__ == "__main__":
    print(a(7, 6))