from typing import List

def duplicateZeros(arr: List[int]) -> None:
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1