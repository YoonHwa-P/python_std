# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

# Polymorphism
# common interface for multiple forms (data types)
# retangle, square, circle, but share color method

class Person:
    def speak(self):
        print("A Person can't speak Korean")

class Korean:
    def speak(self):
        print("Korean can speak korean")

# common interface
def speaking_test(human):
    human.speak()

if __name__ == "__main__":
    person = Person()
    kim = Korean()

    # passing the object
    speaking_test(person)
    speaking_test(kim)