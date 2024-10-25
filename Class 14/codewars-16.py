def high(x):
    return max(x.split(), key=lambda word: sum(ord(c) - 96 for c in word))

print(high("man i need a taxi up to ubud"))
print(high("what time are we climbing up the volcano"))