from sys import argv
import csv


def get_max(sequence, sub):
    print("hello")


def main():
    if len(argv) != 3:
        print("Get your weight up")
    else:
        csvFile = argv[1]
        with open(csvFile) as csv_file:
            data = csv.reader(csv_file)
            for i in data:
                print(i)

        txtFile = argv[2]
        with open(txtFile) as txt_file:
            seq = txt_file.read()

        counter = []
        for i in range(len(seq)):
            print(i)


main()
