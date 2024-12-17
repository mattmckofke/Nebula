def rot13(message):
    result = ""
    for i in message:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) - 65 + 13) % 26 + 65)
            else:
                result += chr((ord(i) - 97 + 13) % 26 + 97)
        else:
            result += i
    return result

print(rot13("test"))
print(rot13("Test"))

import string

def rot132(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    trans = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    return message.translate(str.maketrans(alpha, trans))

print(rot132("test"))
print(rot132("Test"))