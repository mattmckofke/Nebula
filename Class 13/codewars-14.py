def printer_error(s):
    return f"{len([c for c in s if c < 'a' or c > 'm'])}/{len(s)}"