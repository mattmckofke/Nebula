def parse(data):
    result = []
    value = 0
    for i in data:
        if i == "i":
            value += 1
        elif i == "d":
            value -= 1
        elif i == "s":
            value *= value
        elif i == "o":
            result.append(value)
    return result

print(parse("iiisdoso"))
print(parse("iiisdosodddddiso"))

def parse2(data):
    commands = {"i": lambda x: x + 1, "d": lambda x: x - 1, "s": lambda x: x * x}
    result = []
    value = 0
    for command in data:
        if command == "o":
            result.append(value)
        elif command in "ids":
            value = commands[command](value)
            
    return result

print(parse2("iiisdoso"))
print(parse2("iiisdosodddddiso"))