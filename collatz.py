# John Kavanagh
# we need to create a program where the input of a positive integer is required
# integer is considered to be a whole number.
# if the value is even, dividie it by 2
# if it is odd, then multiply it by 3 and then add 1
# program ends when value is 1.

a = input("Type in a positive integer: ")
b= 2

while a != 1:
    if a % b == 0:
        print (a)
        print (a/2)
    else:
        print(a*3 + 1)
