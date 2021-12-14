# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : UTF-8

class Human:

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    human01 = Human(name="A")
    human02 = Human(name="A")

    print(human01 == human02)
    print("human 01 : ", human01)
    print("human 02 : ", human02)