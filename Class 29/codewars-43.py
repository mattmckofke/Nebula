def increment_string(strng):
    if strng and strng[-1].isdigit():
        num = ""
        while strng and strng[-1].isdigit():
            num = strng[-1] + num
            strng = strng[:-1]
        num = str(int(num) + 1).zfill(len(num))
        return strng + num
    else:
        return strng + "1"