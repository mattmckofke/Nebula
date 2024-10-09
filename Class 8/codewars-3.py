def accum(s):
    result = []
    for i in range(len(s)):
        result.append(s[i].upper() + s[i].lower() * i)
    return '-'.join(result)

print("accum: " + accum("abcd"))

def accum2(s):
    return '-'.join([s[i].upper() + s[i].lower() * i for i in range(len(s))])

print("accum2: " + accum2("abcd"))