def solve(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        return s.upper()
    return s.lower()

print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))

def solve2(s):
    return s.upper() if sum(1 for i in s if i.isupper()) > len(s) / 2 else s.lower()

print(solve2("code"))
print(solve2("CODe"))
print(solve2("COde"))
print(solve2("Code"))