def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return [s[i:i+2] for i in range(0, len(s), 2)]

print(solution("abcdef"))
print(solution("abcdefg"))

def solution2(s):
    return [(s + "_")[i:i+2] for i in range(0, len(s), 2)]

print(solution2("abcdef"))
print(solution2("abcdefg"))

from re import findall

def solution3(s):
    return findall(".{2}", s + "_")

print(solution3("abcdef"))
print(solution3("abcdefg"))