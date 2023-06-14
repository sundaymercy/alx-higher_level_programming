#!/usr/bin/python3
def search_replaced(my_list, search, replaced):
    def s_replace(element):
        return (element if element != search else replace)
    return list(map(s_replace, my_list))
