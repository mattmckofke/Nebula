def wave(s):
    if s == "":
        return []
    s = list(s)
    wave = []
    for i in range(len(s)):
        if s[i] == " ":
            continue
        s[i] = s[i].upper()
        wave.append("".join(s))
        s[i] = s[i].lower()
    return wave

print(wave("hello"))
print(wave("hello world"))

def wave2(s):
    return [s[:i] + s[i].upper() + s[i+1:] for i in range(len(s)) if s[i].isalpha()]

print(wave2("hello"))
print(wave2("hello world"))