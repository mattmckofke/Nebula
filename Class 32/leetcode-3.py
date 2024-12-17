from typing import List

def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted(x*x for x in nums)