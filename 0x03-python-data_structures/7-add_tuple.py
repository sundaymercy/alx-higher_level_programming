#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    index = ()
    for x in (tuple_a, tuple_b):
        if len(x) == 0:
            x = (0, 0)
        elif len(x) == 1:
            x = (x[0], 0)
        if index == ():
            index = x
    return x[0] + index[0], x[1] + index[1]
