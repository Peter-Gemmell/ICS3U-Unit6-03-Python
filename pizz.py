#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on may 2022
# This program program creates 10 random numbers & finds largest number

import random


def find_largest(array=[]):
    largest_number = 0
    loop_counter = 0
    while loop_counter < len(array):
        if array[loop_counter] > largest_number:
            largest_number = array[loop_counter]
        loop_counter += 1
    return largest_number


def main():

    # process
    list_numbers = []
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))

    # call functions
    largest_number = find_largest(list_numbers)

    # output
    print("\nThe largest number is {}.".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
