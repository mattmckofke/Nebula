def get_middle(s):
    if (len(s) % 2 == 0):
        return s[(len(s)//2)-1: (len(s)//2)+1]
    else:
        return s[len(s)//2]
    
s = "hell"
s2 = "hello"
print(get_middle(s))
print(get_middle(s2))