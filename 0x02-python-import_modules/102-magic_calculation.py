#!/usr/bin/python3

def magic_calculation(a, b):
    """The python the function that matches the bytecode given."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
