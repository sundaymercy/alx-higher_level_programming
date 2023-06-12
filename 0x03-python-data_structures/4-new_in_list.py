#!/usr/bin/python3
def new_in_list(my_list, y, element):
    new = list(my_list)
    if y < 0 or y > len(my_list) - 1:
        return (new)
    else:
        new[y] = element
        return(new)
