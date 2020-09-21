from datetime import date,datetime

class User:

    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value


if __name__ == "__main__":
    user = User('feta',date(1993,2,12))
    user.age = 30

    print(user.age)
    print(user._age)