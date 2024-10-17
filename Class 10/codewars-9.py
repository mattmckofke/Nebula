def create_phone_number(n):
    for i in range(len(n)):
        n[i] = str(n[i])
    return "(" + "".join(n[0:3]) + ") " + "".join(n[3:6]) + "-" + "".join(n[6:10])

def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))