class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(rem):
            if rem < 0:
                return 0
            if rem == 0:
                return 1

            if rem in memo:
                return memo[rem]

            memo[rem] = dfs(rem -1) + dfs(rem - 2)

            return memo[rem]

        return dfs(n)