class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        s, e = newInterval
        m = 0

        while l <= r:
            m = l + (r - l) // 2

            if intervals[m][0] == s:
                break

            if intervals[m][0] < s:
                l = m + 1
            
            if intervals[m][0] > s:
                r = m - 1
        merged = False
        if l > 0:
            if intervals[l-1][1] >= s:
                l -= 1
                s = intervals[l][0]
                e = max(intervals[l][1], e)
                merged = True
        if merged:
            i = l + 1
        else:
            i = l


        while i < len(intervals) and intervals[i][0] <= e:
            e = max(e, intervals[i][1])
            intervals.pop(i)
        if merged:
            intervals[l] = [s,e]
        else:
            intervals.insert(l, [s,e])
        return intervals
