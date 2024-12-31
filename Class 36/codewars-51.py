def good_vs_evil(good, evil):
    good_vals = [1, 2, 3, 3, 4, 10]
    evil_vals = [1, 2, 2, 2, 3, 5, 10]
    good = sum([int(x) * y for x, y in zip(good.split(), good_vals)])
    evil = sum([int(x) * y for x, y in zip(evil.split(), evil_vals)])
    if good > evil:
        return "Battle Result: Good triumphs over Evil"
    elif good < evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"