from datetime import date


def daysBetweenDates(date1, date2):
    y1, m1, d1 = list(map(int, date1.split('-')))
    y2, m2, d2 = list(map(int, date2.split('-')))

    days = date(y1, m1, d1) - date(y2, m2, d2)

    return abs(days.days)


date1 = "2019-12-14"
date2 = "2019-12-15"
print(daysBetweenDates(date1, date2))
