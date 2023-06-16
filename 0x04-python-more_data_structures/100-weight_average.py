#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = add([a * b for a, b in my_list])
    result = s / add([b for a, b in my_list])
    return result
