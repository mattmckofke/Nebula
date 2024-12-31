def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for i in arr:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))