class parent:
    def func1(self):
        print("This function is in parent class.")


class child(parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(parent):
    def func3(self):
        print("This function is in child 2.")


object1 = child()
object2 = Child2()
object1 .func1()
object1 .func2()
object1 .func1()
object1 .func3()

