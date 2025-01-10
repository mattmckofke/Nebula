from typing import List

def heightChecker(heights: List[int]):
    sort_height = heights.copy()
    sort_height.sort()
    count = 0
    for i in range(len(heights)):
        if sort_height[i] != heights[i]:
            count += 1
    return count