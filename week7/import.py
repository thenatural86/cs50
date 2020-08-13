from cs50 import SQL
from sys import argv, exit
import csv
import cs50


def get_names(full_name):
    names = row["name"].split()
    return names if len(names) >= 3 else [names[0], None, names[1]]


# main function
def main():
    # check to make sure correct number of args in user input
    if len(argv) != 2:
        print("Get your weight up")
        exit(1)


# SQL students databse as db
open("students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")
db.execute(
    "CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

# csv file from user input
csvFile = argv[1]
# open as save as file
with open(csvFile) as file:
    # pass file into DictReader and save a reaer
    reader = csv.DictReader(file)
    # iterate over each row in reader dict
    for row in reader:
        names = get_names(row["name"])
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   names[0], names[1], names[2], row["house"], row["birth"])

if __name__ == "__main__":
    main()
