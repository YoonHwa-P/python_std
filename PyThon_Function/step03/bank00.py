# /c/Users/GREEN/Desktop/python_class/venv/Scripts/python
# -*- coding: utf-8 -*-

class Human:

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    human01 = Human(name="A")
    human02 = Human(name="A")

    print(human01 == human02)
    print("human01: ", human01)
    print("human02: ", human02)

