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
            # create a temp counter var set to 0
            counter = 0
            # while True:
            # while match is true
            while seq[i:j] == sub:
                # update counter
                counter += 1
                # update in to length of string
                i += len(seq)
                j += len(seq)
                # if counter is greater than mxai than update maxi to the value of counter
                if counter > maxi:
                    maxi = counter
        # otherise there is no match ++ vars
        else:
            i += 1
            j += 1
    return maxi


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
            row = next(data)[1:]
            # for i in data:
            #     print(i)

        txtFile = argv[2]
        with open(txtFile) as txt_file:
            # read in entire file at once
            seq = txt_file.read()

            max_data = [get_max(seq, sub) for sub in row]
            print(seq)
            get_max(seq, seq)


if __name__ == "__main__":
    main()
