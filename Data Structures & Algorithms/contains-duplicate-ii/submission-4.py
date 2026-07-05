class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i in range(len(nums)):
            if nums[i] in last_seen and i - last_seen[nums[i]] <= k:
                return True
            else:
                last_seen[nums[i]] = i
        return False