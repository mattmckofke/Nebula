from typing import List

def moveZeroes(nums: List[int]):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums