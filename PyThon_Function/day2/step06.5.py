# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# Nested function 활용 예

def a(x, y):
    """

    :param x: Num
    :param y: Num
    :return:
    """

    if x>5 and x<8 and y<5 and y<8 :
        print(x * y)
    else:
        print("please enter other number")
        raise ValueError("X is {}, y is {}".format(x, y))

if __name__ == "__main__":
    print(a(4,6))