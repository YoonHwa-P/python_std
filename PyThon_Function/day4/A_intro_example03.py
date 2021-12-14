# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

# Methods

class Person:

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def whoAmI(self):
        print("I am Person")

    # instance method
    def singing(self, song):
        return "{} {}을 노래합니다.".format(self.name, song)

    def dancing(self):
        return "{} 현재 춤을 춥니다.".format(self.name)

# Child Class
class Korean(Person):

    def __init__(self, name, age):
        # call super() function
        super().__init__(name, age)
        print("Korean class is ready")

    def whoAmI(self):
        print("I am Korean")

    def study(self):
        print("Fast Runner")

if __name__ == "__main__":
    kim = Korean("Kim", 30)
    person = Person("Kim", 30)
    print(kim.dancing())
    print(kim.singing("사랑"))
    kim.whoAmI()
    person.whoAmI()