"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import math, statistics, numpy as np

Months = {"Jan": 31,
          "Feb": 28,
          "Mar": 31,
          "Apr": 30,
          "May": 31,
          "Jun": 30,
          "Jul": 31,
          "Aug": 31,
          "Sep": 30,
          "Oct": 31,
          "Nov": 30,
          "Dec": 31,
        }

month_keys = list(Months.keys())

              
Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def day_runner(desired_date):
    a = [["Jan", 1, 1900], ["Mon"]]
    
    month = a[0][0]
    DOM = a[0][1]
    year = a[0][2]

    DOW = a[1]

    year_0 = a[0][2]
    Sun_count = 0
    month_count = 0
    Sun_First_count = 0
    dow_temp = False
    
    while year < desired_date[2]:
        if year % 4 == 0:
            Months["Feb"] = 29
        elif year % 1000 and year % 400:
            Months["Feb"] = 29
        else:
            Months["Feb"] = 28
        index = 0
        if year == year_0:
            index = month_keys.index(month)
        while index < len(month_keys):
            month_len = Months[month_keys[index]]
            while DOM < month_len + 1:
                if not dow_temp:
                    DOW = Days[(DOM % 7) - 1]
                else:
                    DOW_0 = Days.index(dow_temp)
                    DOW = Days[(((DOW_0) % 7) - 1)]
                if (DOW == "Sun"):
                    Sun_count += 1
                    if DOM < 2:
                        Sun_First_count += 1
                DOM += 1
                dow_temp = DOW
            index += 1
            DOM = 1
            month_count += 1
        year += 1
        # print(year, Sun_count, Sun_First_count, month_count)
    return Sun_First_count

print(day_runner([31, "Dec", 2000]))
