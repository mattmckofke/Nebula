def in_array(array1, array2):
    x = []
    for i in array1:
        for j in array2:
            if i in j:
                x.append(i)
                break
    return sorted(list(set(x)))

print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))