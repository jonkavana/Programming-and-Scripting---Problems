# John Kavanagh
# need to create a function that finds the square root of any positive number

x = (int(float(input("Type in any positive number: "))))

def sqrt(x):
    return round(x ** (1/2), 1)

# I'd like to prodce an error message if a positive integer isn't entered

print("The square root of", x, "is approximately", sqrt(x))