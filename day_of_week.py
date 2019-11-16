"""
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values 
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
 
Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
"""

import datetime


def dayOfTheWeek(day, month, year):
    date = datetime.datetime(year, month, day)
    day = datetime.datetime.strftime(date, '%A')
    return day


day = 31
month = 8
year = 2019

print(dayOfTheWeek(day, month, year))
