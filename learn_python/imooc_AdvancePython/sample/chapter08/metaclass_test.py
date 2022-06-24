# 类也是对象，type是创建类的类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


if __name__ == "__main__":
    MyClass = create_class("user")
    my_obj = MyClass()
    print(my_obj)
    print(type(my_obj))
