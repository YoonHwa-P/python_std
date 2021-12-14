# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

# Methods

class Person:

    # class attribute
    country = "korean"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def singing(self, song):
        return "{} {}을 노래합니다.".format(self.name, song)

    def dancing(self):
        return "{} 현재 춤을 춥니다.".format(self.name)

if __name__ == "__main__":

    # instance the object
    kim = Person("Kim", 30)

    # call our instance methods
    print(kim.singing("행복"))
    print(kim.dancing())