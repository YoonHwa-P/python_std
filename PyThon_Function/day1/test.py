#/c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-
# 다른 file에 함수 불러오기

import step02_basic
import inspect

docstring = inspect.getsource(step02_basic.cnt_letters)

if __name__ == "__main__":
    border = "*" * 20
    print('{}\n{}\n{}'.format(border, docstring, border))