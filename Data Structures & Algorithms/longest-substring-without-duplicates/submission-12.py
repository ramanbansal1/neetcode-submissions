class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        last_seen = {}
        l = r = 0
        while l <= r and r <= len(s) - 1:
            if s[r] in last_seen and last_seen[s[r]] >= l:
                l = last_seen[s[r]] + 1
            last_seen[s[r]] = r
            max_length = max(max_length, r-l + 1)
            print(l, r, max_length)
            r += 1

        return max_length 