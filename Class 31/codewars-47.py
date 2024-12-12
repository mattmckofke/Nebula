def spoonerize(words):
    words = words.split()
    return words[1][0] + words[0][1:] + " " + words[0][0] + words[1][1:]

print(spoonerize("nit picking"))
print(spoonerize("wedding bells"))