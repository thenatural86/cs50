from sys import argv
import csv

# takes in sequence and substring - calculate max number of times sub is repeated in seq


def get_max(seq, sub):
    i = 0
    j = len(sub)
    maxi = 0


def main():
    if len(argv) != 3:
        print("Get your weight up")
    else:
        csvFile = argv[1]
        # if there is an error, with open will close file
        with open(csvFile) as csv_file:
            # file is read in to memeory via csv reader
            # and return iterable object
            data = csv.reader(csv_file)
            # need to eleminate first row which is a header
            # for i in data:
            #     print(i)

        txtFile = argv[2]
        with open(txtFile) as txt_file:
            # read in entire file at once
            seq = txt_file.read()
            print(seq)
            get_max(seq, data)


main()
