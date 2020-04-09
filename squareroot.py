# John Kavanagh
# need to create a function called sqrt, that finds the square root of any positive number

#def sqrt(x):
#    return x ** (1/2)

x = (float(input("Type in any positive number: ")))

def sqrt(x):
    return x ** (1/2)

print("The square root of", x, "is approximately", sqrt(x))
