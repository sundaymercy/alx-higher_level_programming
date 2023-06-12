#!/usr/bin/python3
def replace_in_list(my_list, y, element):
    if y < 0 or y > len(my_list) - 1:
        return (my_list)
    else:
        my_list[y] = element
        return (my_list)
