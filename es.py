# John Kavanagh
# moby-dick.txt
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# read in a text file, # count of the letter e, input of file from CLI

# reading in a file and the paramters: https://realpython.com/read-write-files-python/
# reading material on standard library: https://docs.python.org/3/library/index.html
# additional material on CSV Structure: https://realpython.com/python-csv/
# Reading on how to write in via the CLI: https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162
# reading on how to iterate over lines: https://docs.python.org/3/library/fileinput.html
# Reading - Library on Sys: https://www.python-course.eu/sys_module.php
# with open functionality https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
# reading files on JSON structures https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files


# Approach Number 1
# with open (input('work_file')) as f:
   # read_date = f.read()
# f.closed    

#Approach NUmber 2
file = open('moby11b.txt', 'r')

for line in file.readlines():
    print(line)

#Approach Number 2a
#line = file.readline()
#f = line.__eq__("**The Project Gutenberg Etext of Moby Dick, by Herman Melville**\n")

#print(f)

# Approach Number 3
#file = open('C:\Users\jonka\Desktop\Programming-and-Scripting---Problems\txt file', 'r')
# type(file)

# Testing Iterative Count
# count = 10
# while( count > 0):
    # print("hello world")
    # count = count - 1

# print("finished")