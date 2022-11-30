#!/usr/bin/python3

for (i,j) in [(i,j) for i in range(0, 10) for j in range(0, 10)]:
        if (i + j == 18):
            print("{}{} ".format(i,j))
        else:
            print("{}{}, ".format(i, j), end = "")
