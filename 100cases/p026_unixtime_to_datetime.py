import datetime


uninx_time = 1620747647

datetime_obj = datetime.datetime.fromtimestamp(uninx_time)
datetime_str = datetime_obj.strftime("%Y-%m-%d")
print(datetime_str)
