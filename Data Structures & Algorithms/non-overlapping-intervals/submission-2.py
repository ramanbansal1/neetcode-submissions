class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[0])
        removals = 0

        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                removals += 1
                if curr[1] <= prev[1]:
                    prev = curr
            else:
                prev = curr

        return removals 