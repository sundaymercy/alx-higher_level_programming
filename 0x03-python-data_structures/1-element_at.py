#!/usr/bin/python3
def element_at(my_list, y):
    if y < 0:
        return (None)
    elif y > len(my_list) - 1:
        return (None)
    else:
        return (my_list[y])
