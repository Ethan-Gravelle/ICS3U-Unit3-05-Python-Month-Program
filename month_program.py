#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 6, 2020
# This program determines the month

def main():
    # this function determines the month.

    # input
    number = int(input("Enter a number of a month (ex: 3 for March): "))
    # process & output
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
    else:
        print("Invalid Entry.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
