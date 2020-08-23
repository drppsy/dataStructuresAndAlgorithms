import class_method
import datetime

class User:

    def __init__(self,brithday):
        self.__brithday = class_method.Date.parse_str(brithday)

    def get_age(self):
        age = int(datetime.datetime.now().strftime("%Y")) - int(self.__brithday.year)
        return age


if __name__ == "__main__":
    user = User("1993-2-12")
    age = user.get_age()
    print(age)

    print(user._User__brithday)
