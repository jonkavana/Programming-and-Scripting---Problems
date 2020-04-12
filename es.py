# John Kavanagh
# moby-dick.txt
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.

with open (input('workfile')) as f:
    read_date = f.read()

f.closed    