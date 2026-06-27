class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not (0 in nums):
            return True

        if len(nums) == 1:
            return True
        counter = len(nums) - 2
        goal = 1
        result = False
        while counter >= 0:

            if nums[counter] >= goal:
                counter -= 1
                goal = 1
                result = True
            else:
                result = False
                counter -= 1
                goal += 1

        return result