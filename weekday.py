# John Kavanagh
# Create a program that will identify if a day is a weekday or weekend

import datetime
import calendar

L = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
dayno=datetime.datetime.today().weekday()
print("Today is", L[dayno])

if dayno < 4:
    print("Hauld your horeses")
else:
    print("You've made it ,now reward yourself.")
