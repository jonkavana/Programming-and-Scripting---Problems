# John Kavanagh
# Input required is a positive integer
# integer is considered to be a whole number.
# Even numbers will be divided by 2
# Odd numbers are trebled and one is added to the result
# program ends when value is 1.

a = int(input("Type in a positive integer: "))
b = 2

while a > 1:
    if a % b != 0:
        a = ((a*3)+1)
    else:
        a = (a/2)
    print(a)