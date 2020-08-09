from sys import argv
import csv

# takes in sequence and substring - calculate max number of times sub is repeated in seq


def get_max(seq, sub):
    i = 0
    # set var to length of substring
    j = len(sub)
    maxi = 0

    # iterate through sequence
    for i in range(len(seq)):
        # the substring from seq[from the ith character: up through but not including the jth character]
        # is equal to the substring that is passed in
        if seq[i:j] == sub:
            # do this thing
            print(i)


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
            get_max(seq, seq)


if __name__ == "__main__":
    main()
