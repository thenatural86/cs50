from sys import argv
import csv

if len(argv) != 3:
    print("Get your weight up")
else:
    csvFile = open(argv[1])
    txtFile = open(argv[2])
    # reads one row at a time
    data = csv.reader(csvFile)
    # reads whole file at once
    seq = txtFile.read()

    length = len(seq)
    # print(length)

    for i in range(length):
        print(i)
        for j in range(length):
            # if seq[i:j] == seq[i + 4]:
            print(seq[i:j])

        # need to find most repeating substring
# print(seq)
