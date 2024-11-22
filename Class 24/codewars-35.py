def remove_duplicate_words(s):
    return " ".join(sorted(set(s.split()), key=s.index))

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))

def remove_duplicate_words2(s):
    return " ".join(dict.fromkeys(s.split()))

print(remove_duplicate_words2("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words2("my cat is my cat fat"))