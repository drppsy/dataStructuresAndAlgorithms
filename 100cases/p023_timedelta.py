import datetime


birthday = '1993-02-12'

birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
current_day = datetime.datetime.now()

print(current_day - birthday)
print((current_day - birthday).days)