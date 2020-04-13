# John Kavanagh
# need to create a function that finds the square root of any positive number

# x = (int(float(input("Type in any positive number: "))))
userInput = input("Type in any positive number: ")
value = float(userInput)


def sqrt(value):
    if value < 0:
        raise ValueError("Input needs to be a postive number.")
    return round(value ** (1/2), 1)

print("The square root of", value, "is approximately", sqrt(value))