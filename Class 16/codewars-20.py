def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    else:
        mid = len(encrypted_text) // 2
        first = encrypted_text[:mid]
        last = encrypted_text[mid:]
        decrypted_text = ''
        for i in range(mid):
            decrypted_text += last[i] + first[i]
        if len(first) != len(last):
            decrypted_text += last[-1]
        return decrypt(decrypted_text, n - 1)
    
def encrypt(text, n):
    if n <= 0:
        return text
    else:
        encrypted_text = ''
        for i in range(1, len(text), 2):
            encrypted_text += text[i]
        for i in range(0, len(text), 2):
            encrypted_text += text[i]
        return encrypt(encrypted_text, n - 1)