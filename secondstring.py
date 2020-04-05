# John Kavanagh
# The quick brown fox jumps over the lazy dog
# we need to reverse the order of the sentence, but only include the second letter

str = (input("Type in any sentence you so choose:"))
stringlength = len(str)

slicedstring = str[::-2]
print(slicedstring)