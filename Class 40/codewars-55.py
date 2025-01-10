def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0
    lengths = {}
    
    for arr in array_of_arrays:
        if not arr:
            return 0
        lengths[len(arr)] = arr
        
    start = min(lengths.keys())
    end = max(lengths.keys())
    idx = -1
    i = start
    
    while i < end:
        i += 1
        if lengths.get(i):
            if idx > 0 and i > idx + 1:
                return idx
        else:
            idx = i
        
    return idx