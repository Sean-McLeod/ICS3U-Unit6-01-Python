#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program calculates the average of 10 random numbers

import random


def main():
    # this function calculates the average of 10 random numbers

    array_random_number = []
    average = 0

    for loop_counter in range(0, 10):
        single_random_number = random.randint(1, 100)
        array_random_number.append(single_random_number)
        average = average + (array_random_number[loop_counter])
        print("The random number is {}".format(single_random_number))
    print("")

    average = average/10
    # output
    print("The average is: {}".format(average))


if __name__ == "__main__":
    main()
