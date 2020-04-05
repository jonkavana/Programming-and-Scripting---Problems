# need to work out how the datetime obkect works

import datetime

L = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
dayno=datetime.datetime.today().weekday()

print("Today is", L[dayno])

if dayno < 4:
    print("Hauld your horeses")
else:
    print("induldge")