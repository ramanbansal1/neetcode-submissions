class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        # Maximum frequency
        max_freq = max(freq.values())

        # Number of tasks having the maximum frequency
        max_count = 0
        for count in freq.values():
            if count == max_freq:
                max_count += 1

        # Greedy formula
        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(intervals, len(tasks))