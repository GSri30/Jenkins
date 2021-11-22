#!/usr/bin/python3
# Program for calculating mean of list of numbers

def mean(numbers):
    if(len(numbers)):
        return sum(numbers)/len(numbers)
    return 0