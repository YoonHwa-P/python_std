# /Users/evan/Desktop/python_class_edu/venv/bin/python
# -*- conding: utf-8 -*-

class Person:
    """
    사람을 표현하는 클래스

    ...

    Attributes
    ----------
    name : str
        name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age
    """

    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the person object

        Parameters
        ----------
            name : str
                name of the person
            age : int
                age of the person
        """

        self.name = name
        self.age = age

    def info(self, additional=None):
        """
        Prints the person's name and age

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name}. I am {self.age} years old. ' + additional)

if __name__ == "__main__":
    person = Person("Evan", age = 300)
    person.info("나의 직장은 어디?")
    print(Person.__doc__)
    help(Person)
