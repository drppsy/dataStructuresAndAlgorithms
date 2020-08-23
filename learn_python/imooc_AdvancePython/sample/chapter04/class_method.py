class Date:

    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

    # 静态方法
    @staticmethod
    def parse_from_string(date_str):
        year,month,day = tuple(date_str.split("-"))
        return Date(year,month,day)

    # 类方法
    @classmethod
    def parse_str(cls,date_str):
        year,month,day = tuple(date_str.split("-"))
        return cls(year,month,day)

    # 静态方法
    @staticmethod
    def is_valid(date_str):
        year,month,day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month) > 0 and int(month) < 13) and (int(day) > 0 and int(day) < 32):
            return True
        else:
            return False


if __name__ == "__main__":
    date = Date(2020,8,23)
    print(date)

    date2 = Date.parse_from_string("2020-8-23")
    print(date2)

    date3 = Date.parse_str("2020-8-23")
    print(date3)

    print(Date.is_valid("2020-8-32"))