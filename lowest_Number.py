#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on may 2022
# This program program creates 10 random numbers & finds largest number

import random


def find_lowest(list_numbers):
    # this function finds the highest number
    lowest_number = list_numbers[0]
    # process
    for loop_num in list_numbers:
        if loop_num < lowest_number:
            lowest_number = loop_num
    return lowest_number


def main():
    # this function gathers the 10 random numbers
    list_numbers = []
    total = 0
    counter = 0
    rounded = 0
    # this loop gathers the 10 numbers, randomly through 1 to 100
    for counter in range(10):
        random_number = random.randint(0, 100)
        list_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))
    # output
    lowest_number = find_lowest(list_numbers)
    print("\nThe lowest number is {0}".format(lowest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
