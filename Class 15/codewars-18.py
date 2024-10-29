def order(sentence):
    if sentence == "":
        return ""
    words = sentence.split()
    result = []
    for i in range(1, 10):
        for word in words:
            if str(i) in word:
                result.append(word)
    return " ".join(result)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))

def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda word:sorted(word)))

print(order2("is2 Thi1s T4est 3a"))
print(order2("4of Fo1r pe6ople g3ood th5e the2"))