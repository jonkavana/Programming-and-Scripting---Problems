# John Kavanagh
# Create a program that will identify if a day is a weekday or weekend
# Essential reading in order to complete task: https://realpython.com/python-lists-tuples/
# Added material to provide greater context: https://www.geeksforgeeks.org/python-set-3-strings-lists-tuples-iterations/
# further material was taken from the World wind tour of python: https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# Added material in relation to the dictionaries: https://realpython.com/python-dicts/
# Acknowledging that there needs to be the import of datetime and calendar completed first.

import datetime
import calendar

L = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
dayno=datetime.datetime.today().weekday()
#syntax of creating a datetime.datetime.weekday took a lot of iteration to understand. 

print("Today is", L[dayno])
# Need to be able to print to the screen a message based on the number aligned to the days.
if dayno < 4:
    print("It's not the weekend yet, but soon it will be.")
else:
    print("You've made it, now reward yourself.")
