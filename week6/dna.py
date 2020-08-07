from sys import argv
import csv

if len(argv) != 3:
    print("Get your weight up")
else:
    file = open(argv[1], "r")
    print("Yeah kid!", argv[1])
