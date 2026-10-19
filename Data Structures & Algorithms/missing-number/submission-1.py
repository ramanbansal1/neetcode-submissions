class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)
        sum_exp = max_ * (max_ + 1)/2
        s = sum(nums)

        if max_ < len(nums):
            return len(nums)
        return int(sum_exp) - s