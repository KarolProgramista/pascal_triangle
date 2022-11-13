#!/bin/python3

pascal_tree_unformated_file = open("pascaltree.txt", "r")
pascal_tree_formated_file = open("pascaltree_f.txt", "w")

n = int(pascal_tree_unformated_file.readline())

lines = pascal_tree_unformated_file.readlines()

i=0
last_line = lines[-1].split()
longest_line = len(lines[-1])
longest = len(last_line[len(last_line)//2])
lines_biger = []

for line in lines:
    line_str = ""
    split_line = line.split()
    for number in split_line:
        line_str += number+" "*(longest-len(number)+1)

    lines_biger.append(line_str)

longest_line = len(lines[-1])
for line in lines_biger:
    print(" "*int((longest_line-len(line))//2)+line)
#for line in lines:
#    split_line = line.split()
#    print(" "*(n-i+(longest_line-len(line))//2), end='')
#    for number in split_line:
#        print(" "*(longest - len(number)+1)+number+" "*(longest - len(number)+1), end='')
#
#    print("")
#    i+=1

pascal_tree_unformated_file.close()
pascal_tree_formated_file.close()
