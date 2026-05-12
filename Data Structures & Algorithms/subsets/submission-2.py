class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            for j in result.copy():
                new_subset = j + [i]
                result.append(new_subset)
        
        return result