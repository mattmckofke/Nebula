from typing import List

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        acc = 0
        most = 0
        
        for num in nums:
            if num == 1:
                acc += 1
                
            else:
                acc = 0
            most = max(most, acc)
        return most