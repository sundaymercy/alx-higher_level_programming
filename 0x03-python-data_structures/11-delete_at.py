#!/usr/bin/python3
def delete_at(my_list=[], y=0):
    if y < 0 or y > len(my_list) - 1:
        return my_list
    del(my_list[y])
    return my_list
