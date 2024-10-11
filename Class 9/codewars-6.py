def open_or_senior(data):
    result = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]