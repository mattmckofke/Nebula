def switcheroo(s):
    return s.translate(str.maketrans("ab", "ba"))

print(switcheroo("abcba"))
print(switcheroo("caaababbbcc"))