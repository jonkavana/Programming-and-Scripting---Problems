# John Kavanagh
# need to create a function that finds the square root of any positive number
# Reading material has been taken from: https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# There is a dedicated chapter to it, pg 41. 
# Additioal material to be seen here: https://www.learnpython.org/en/Functions

# x = (int(float(input("Type in any positive number: "))))
userInput = input("Type in any positive number: ")
value = float(userInput)

# defining a squareroot funciton doc: https://www.w3schools.com/python/python_functions.asp
def sqrt(value):
    if value < 0:
        raise ValueError("Input needs to be a postive number.")
# This custom erro has been introduced if the user tries to enter a negative value. 
    return round(value ** (1/2), 1)

print("The square root of", value, "is approximately", sqrt(value))