class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def splits(nums, max_):
            ss = 1
            sum_ = 0
            for i in nums:
                if sum_ + i > max_:
                    ss += 1
                    sum_ = i
                else:
                    sum_ += i
            return ss


        while l <= r:
            m = l + (r - l) // 2

            if splits(nums, m) > k:
                l = m + 1
            
            else:
                r = m - 1

        return l
            

