def filter_list(l):
    'return a new list with the strings filtered out'
    return [x for x in l if isinstance(x, int)]

l = [1,2,'a','b']