def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0 and x is not False)