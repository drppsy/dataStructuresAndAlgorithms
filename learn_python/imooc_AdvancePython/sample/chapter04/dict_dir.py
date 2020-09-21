class Person:
    '''
    人
    '''
    name = "user"

class Student(Person):

    def __init__(self,school_name):
        self.school_name = school_name


if __name__ == "__main__":
    stu = Student("慕课网")
    print(stu.__dict__)
    print(dir(stu))
    print(Person.__dict__)
    print(dir(Person))

    alist = [1,2]
    print(dir(alist))
