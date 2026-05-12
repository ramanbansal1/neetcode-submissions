class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(remain, path, start):

            if remain == 0:
                ans.append(path)
                return

            if remain < 0:
                return

            for i in range(start, len(nums)):
                dfs(remain - nums[i], path + [nums[i]], i)

        dfs(target, [], 0)

        return ans