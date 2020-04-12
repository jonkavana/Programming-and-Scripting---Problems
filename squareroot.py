# John Kavanagh
# need to create a function that finds the square root of any positive number

x = (int(float(input("Type in any positive number: "))))

def sqrt(x):
    if x < 0:
        raise ValueError("Input needs to be a postive number.")
    return round(x ** (1/2), 1)

print("The square root of", x, "is approximately", sqrt(x))