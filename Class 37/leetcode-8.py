from typing import List

def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False

def checkIfExist2(arr: List[int]) -> bool:
    for num in arr:
        if num == 0 and arr.count(0) > 1:
            return True
        if num != 0 and num * 2 in arr:
            return True
    return False