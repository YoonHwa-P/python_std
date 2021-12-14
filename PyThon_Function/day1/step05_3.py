# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-
# context manager file create

import contextlib

@contextlib.contextmanager
def my_context():
    print("hi hello? this is first greeting")
    yield 10
    print("Good bye")

def main():
    with my_context() as temp:
        print("temp 인사말{}".format(temp))

if __name__ == "__main__":
    main()