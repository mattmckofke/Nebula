def generate_hashtag(s):
    if s == "":
        return False
    s = s.split()
    s = [i.capitalize() for i in s]
    s = "#" + "".join(s)
    if len(s) > 140:
        return False
    return s

print(generate_hashtag("Hello there thanks for trying my Kata"))
print(generate_hashtag("Hello        World"))
print(generate_hashtag(""))

def generate_hashtag2(s):
    return '#' + s.strip() if 0 < len(s) <= 140 else False

print(generate_hashtag2("Hello there thanks for trying my Kata"))
print(generate_hashtag2("Hello        World"))
print(generate_hashtag2(""))