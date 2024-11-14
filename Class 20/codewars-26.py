def make_readable(seconds):
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(make_readable("0"))
print(make_readable("60"))
print(make_readable("86399"))

def make_readable2(seconds):
    return "{:02}:{:02}:{:02}".format(int(seconds) // 3600, int(seconds) // 60 % 60, int(seconds) % 60)

print(make_readable2("0"))
print(make_readable2("60"))
print(make_readable2("86399"))