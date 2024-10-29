def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")

print(is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]))
print(is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]))
print(is_valid_walk(["w"]))

def is_valid_walk2(walk):
    return False if len(walk) != 10 else walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")

print(is_valid_walk2(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]))
print(is_valid_walk2(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]))
print(is_valid_walk2(["w"]))