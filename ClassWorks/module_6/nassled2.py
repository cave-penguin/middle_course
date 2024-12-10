class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print("Hello")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human):
    pass
    # arms = False
    # def about(self):
    #     print('Im a student')


class Teacher(Human):
    pass


human = Human()

student = Student()
