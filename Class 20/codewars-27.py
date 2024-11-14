def friend(x):
    return [i for i in x if len(i) == 4]

print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(["Ryan", "Jimmy", "abc", "d"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))