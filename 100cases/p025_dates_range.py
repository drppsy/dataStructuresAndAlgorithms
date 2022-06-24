import datetime


def get_date_range(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    each_dates = []
    each_date = start_date
    while each_date <= end_date:
        each_dates.append(each_date.strftime("%Y-%m-%d"))
        each_date = each_date + datetime.timedelta(days=1)
    return each_dates

print(get_date_range('2022-06-15', '2022-06-22'))