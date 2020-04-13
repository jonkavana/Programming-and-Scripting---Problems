# John Kavanagh
# we need to reverse the order of the sentence, but only include the second letter
# Implement the indeixing and slicing principle - https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf


L = (input("Type in any sentence you so choose:"))

# the variable L has been introduced as a container for the user input. i.e. the sentence that they wish to type.

# Using this input, we now run it through the script to reverse its order and display every second number.

print(L[::-2])