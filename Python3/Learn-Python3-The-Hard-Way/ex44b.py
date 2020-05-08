class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("Child override()")

dad = Parent()
son = Child()

dad.override()
son.override()