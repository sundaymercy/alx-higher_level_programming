#!/usr/bin/python3
def uniq_sum(my_list=[]):
    sum = 0
    for unint in set(my_list):
        sum += unint
    return sum
