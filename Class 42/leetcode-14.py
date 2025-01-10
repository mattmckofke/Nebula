from typing import List

def thirdMax(nums: List[int]):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 3:
        return nums[-1]
    return nums[-3]