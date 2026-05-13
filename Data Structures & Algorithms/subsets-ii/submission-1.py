class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, i=0):
            res.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                path.append(nums[j])
                backtrack(path, j+1)
                path.pop()
        backtrack([])
        return res