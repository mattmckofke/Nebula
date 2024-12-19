def encode(st):
    x = {"a": "1",
         "e": "2",
         "i": "3",
         "o": "4",
         "u": "5"}
    for vowel in x:
        st = st.replace(vowel, x[vowel])
            
    return st

def decode(st):
    x = {"1": "a",
         "2": "e",
         "3": "i",
         "4": "o",
         "5": "u"}
    for vowel in x:
        st = st.replace(vowel, x[vowel])
            
    return st

print(encode("hello"))
print(decode("h2ll4"))

def encode(st):
    return st.translate(str.maketrans("aeiou", "12345"))

def decode(st):
    return st.translate(str.maketrans("12345", "aeiou"))

print(encode("hello"))
print(decode("h2ll4"))