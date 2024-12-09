class Human:
    head = True
    say = 'Im a human'

    # def __init__(self):
    #     self.about()

    def say_hello(self):
        print('Hello')

    def about(self):
        print(self.say)


class Student(Human):
    say = 'Im a student'
    # def about(self):
    #     print(self.say)


class Teacher(Human):
    say = 'Im a teacher'
    # def about(self):
    #     print(self.say)


human = Human()
student = Student()
teacher = Teacher()

human.about()
student.about()
teacher.about()


