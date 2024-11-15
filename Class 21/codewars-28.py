def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 3))

def longest_consec2(starr, k):
    if not starr or k > len(starr) or k <= 0:
        return ""
    return max(["".join(starr[i:i+k]) for i in range(len(starr)-k+1)], key=len)

print(longest_consec2(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec2(["zone", "abigail", "theta", "form", "libe", "zas"], 3))