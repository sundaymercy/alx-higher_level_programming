#!/usr/bin/python3
def safe_print_list_int(my_list=[], x=0):
    count = 0
    for int_str in range(x):
        try:
            print("{:d}".format(my_list[int_str]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    prt()
    return count
