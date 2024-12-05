def sum_pairs(ints, s):
    seen = set()
    for i in ints:
        if s - i in seen:
            return [s - i, i]
        seen.add(i)
    return None