def solve(strings: list[str]) -> list[str]:
    return [sum(1 for i, c in enumerate(s) if ord(c.lower()) - 96 == i + 1) for s in strings]

print(solve(["abode","ABc","xyzD"]))