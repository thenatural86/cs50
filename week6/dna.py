from sys import argv
import csv

# takes in sequence and substring - calculate max number of times sub is repeated in seq


def get_max(seq, sub):
    i = 0
    # set var to length of substring
    j = len(sub)
    maxi = 0
    # iterate through sequence
    for x in range(len(seq)):
        # the substring from seq[from the ith character: up through but not including the jth character]
        # is equal to the substring that is passed in
        if seq[i:j] == sub:
            # create a temp counter var set to 0
            counter = 0
            # while match is true
            while seq[i:j] == sub:
                # update counter
                counter += 1
                # update in to length of string
                i += len(sub)
                j += len(sub)
                # if counter is greater than mxai than update maxi to the value of counter
                if counter > maxi:
                    maxi = counter
        # otherise there is no match ++ vars
        else:
            i += 1
            j += 1
    return maxi


def print_match(data, max_data):
    for i in data:
        person = i[0]
        values = [int(j) for j in i[1:]]
        if values == max_data:
            print(person)
            return
    print("Nope")


def main():
    if len(argv) != 3:
        print("Get your weight up")
        exit(1)

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
            # list comprehession
            max_data = [get_max(seq, sub) for sub in row]

        print_match(data, max_data)


if __name__ == "__main__":
    main()
