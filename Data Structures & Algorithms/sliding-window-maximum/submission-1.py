from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        upper = deque(sorted(range(len(nums[:k])), key=lambda i: nums[:k][i], reverse=True))
        result = [nums[upper[0]]]

        for i in range(k, len(nums)):
            while len(upper) and nums[upper[-1]] < nums[i]:
                upper.pop()
            upper.append(i)
            while upper[0] <= i - k:
                upper.popleft()
            result.append(nums[upper[0]])
        
        return result
