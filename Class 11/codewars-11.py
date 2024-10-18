def alphabet_position(text):
    result = []
    for c in text.lower():
        if c.isalpha():
            position = ord(c) - 96
            result.append(str(position))
    return ' '.join(result)

print(alphabet_position("The sunset sets at twelve o' clock."))