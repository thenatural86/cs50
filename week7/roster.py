# TODO
from sys import argv, exit
from cs50 import SQL
import csv


def main():
    if len(argv) != 2:
        print("nope")
        exit(1)

    # open("students.db", "w")
    db = SQL("sqlite:///students.db")
    house = argv[1]
    data = db.execute(
        "SELECT * FROM students WHERE house = ? ORDER BY last, first", house)
    for row in data:
        first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
        print(f"{first} {middle + ' ' if middle else ''}{last} {birth}")


if __name__ == "__main__":
    main()
