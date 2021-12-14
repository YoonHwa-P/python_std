#/c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

import sys

import namespace as namespace

a= "Python"
b= a
c= a
a= "python"
print(f'a=[a], b=[b], c=[c]')



print(sys.getrefcount(a),sys.getrefcount(b),sys.getrefcount(c))
print(a)


import keyword
import pprint as pp

pp.pprint(keyword.kwlist)

print("**********")
i = 10
print(id(i))
i += 1
print(id(a))
print("**********")

data = 10, 20, 30
first, second, third = data
print(first, second, third)


def function():
    a = 10
    b = 20
    print(locals())
    del b
    print(locals())

function()

print(type(a))