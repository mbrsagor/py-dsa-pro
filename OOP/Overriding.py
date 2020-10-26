class Human(object):

    def say_hello(self):
        print("Hello I'm calling from `Human` class method")


class Teacher(Human):

    def say_hello(self, name="sagor"):
        super(Teacher, self).say_hello()
        print(f"Hey student I'm {name} from class method")


if __name__ == '__main__':
    t1 = Teacher()
    t1.say_hello()
