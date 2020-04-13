# John Kavanagh
# moby-dick.txt
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# read in a text file 
# count of the letter e
# input of file from CLI

# with open (input('work_file')) as f:
   # read_date = f.read()
# f.closed    

file = open('moby11b.txt', 'r')

for line in file.readlines():
    print(line)

#line = file.readline()
#f = line.__eq__("**The Project Gutenberg Etext of Moby Dick, by Herman Melville**\n")

#print(f)
#file = open('C:\Users\jonka\Desktop\Programming-and-Scripting---Problems\txt file', 'r')
# type(file)

# count = 10
# while( count > 0):
    # print("hello world")
    # count = count - 1

# print("finished")