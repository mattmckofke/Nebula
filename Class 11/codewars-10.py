def digital_root(n):
    if n > 9:
        return digital_root(n//10+n%10)
    else: 
        return n

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))