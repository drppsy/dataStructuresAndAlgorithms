import datetime


def get_diff_date(pdate, days):
    pdate = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    date_gap = datetime.timedelta(days=days)
    target_date = pdate - date_gap
    return datetime.datetime.strftime(target_date, "%Y-%m-%d")


print(get_diff_date("2022-06-22", days=1))
print(get_diff_date("2022-06-22", days=7))
print(get_diff_date("2022-06-22", days=23))