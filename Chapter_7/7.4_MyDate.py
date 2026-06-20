# Define a date class named MyDate with three attributes: year, month and day. It also contains a method to calculate the date of the next day and a method to print the date.

import datetime
class MyDate:
    def __init__(self):
        t = datetime.datetime.now()
        self.MyYear = t.year
        self.MyMonth = t.month
        self.MyDay = t.day
    def NextDay(self):
        TotalDays = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],\
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
        self.MyDay = self.MyDay + 1
        leap =  ((self.MyYear % 400==0) or (self.MyYear%4==0 and self.MyYear%100!=0))
        if self.MyDay > TotalDays[leap][self.MyMonth-1]:
            self.MyDay = 1
            self.MyMonth = self.MyMonth + 1
            if self.MyMonth > 12:
                self.MyMonth = 1
                self.MyYear += 1
    def Disp(self):
        print("%d, %d, %d"%(self.MyYear, self.MyMonth, self.MyDay))

d = MyDate()
d.NextDay()
d.Disp()