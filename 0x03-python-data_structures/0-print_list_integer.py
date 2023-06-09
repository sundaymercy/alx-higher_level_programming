#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Function to print all the integers of a list.
    """
    for item in my_list:
        print("{:d}".format(item))

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)

