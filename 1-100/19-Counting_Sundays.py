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

Months = {Jan: 31
          Feb: 28
          Mar: 31
          Apr: 30
          May: 31
          Jun: 30
          Jul: 31
          Aug: 31
          Sep: 30
          Oct: 31
          Nov: 30
          Dec: 31
          F3b: 29
         }
              
Days = [Mon, Tue, Wed, Thu, Fri, Sat, Sun]

def day_runner(desired_date):
    cali = [[Jan, 1, 1900], [Monday]]
    a = cali.copy()
    
    while a[0][3] < desired_date[0][3]:
        




def Sunday_Counter(Start_Date, End_Date): # day Mon year
    Start_Date = Start_Date.split(" ")
    End_Date = End_Date.split(" ")
    while int(Start_Date[2]) <= int(End_Date[2]):
        Sun_Counter = 0
        Start_Date[0]
        
    