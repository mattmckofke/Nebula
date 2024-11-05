def rgb(r, g, b):
    s = ""
    for i in [r, g, b]:
        if i < 0:
            s += "00"
        elif i > 255:
            s += "FF"
        else:
            s += hex(i)[2:].upper().zfill(2)
    return s

print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))

def rgb2(r, g, b):
    return "".join([format(min(max(i, 0), 255), "02X") for i in [r, g, b]])

print(rgb2(0, 0, 0))
print(rgb2(1, 2, 3))
print(rgb2(255, 255, 255))
print(rgb2(254, 253, 252))