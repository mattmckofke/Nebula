def to_camel_case(text):
    if text == "":
        string = text.replace("-", " ").replace("_", " ").split()
    return string[0] + "".join([word.capitalize() for word in string[1:]])

print(to_camel_case("the-stealth-warrior"))  
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case(""))

def to_camel_case(text):
    return "" if not text else text[0] + text.title()[1:].replace("_", "").replace("-", "")

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case(""))