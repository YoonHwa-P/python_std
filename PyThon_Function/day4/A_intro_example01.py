# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

# A class is a blueprint for the object
# Object: an object (instance) is an instantiation of a class.

class Person:

    # class attribute
    country = "korean"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    kim = Person("kim", 100)
    lee = Person("lee", 100)

    # access the class attributes
    print("kim은 {}".format(kim.__class__.country))
    print("lee는 {}".format(lee.__class__.country))

    # country chagne
    kim.__class__.country = "American"
    # access the class attributes
    print("kim은 {}".format(kim.__class__.country))

    lee.__class__.country = "Japanese"
    print("lee는 {}".format(lee.__class__.country))

