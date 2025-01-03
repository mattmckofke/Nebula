from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr)
    max_right = [0] * n
    max_right[-1] = -1
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], arr[i+1])
    return max_right

print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([400]))

def replaceElements2(arr: List[int]) -> List[int]:
    curr_max = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > curr_max:
            curr_max, arr[i] = arr[i], curr_max
        else:
            arr[i] = curr_max

    return arr

print(replaceElements2([17,18,5,4,6,1]))
print(replaceElements2([400]))