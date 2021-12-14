# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# decorator를 이해 하기 위한 4가지 개념

"""
1. 함수 : 객체로서의 함수
2. nested 함수
3. nonlocal Variables
4. Closures
"""


def two_args(func):
    return func

@two_args # <--함수

def add(a, b):
   return a + b

if __name__ == "__main__":
    print(add(1,2))



