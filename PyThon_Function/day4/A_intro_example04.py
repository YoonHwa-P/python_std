# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

# Data Encapsulation in Python

class TV:

    def __init__(self):
        self.__maxprice = 500 # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

if __name__ == "__main__":
    tv = TV()
    tv.sell()

    # change thje price
    # 바뀌지 않음
    tv.__maxprice = 1000
    tv.sell()

    # using setter function
    # 바뀜
    tv.setMaxPrice(1000)
    tv.sell()