import heapq
from collections import deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequencies
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Max heap (negative frequencies)
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)

        cooldown = deque()   # (ready_time, freq, char)
        result = []
        time = 0

        while heap or cooldown:
            # Release characters whose cooldown has finished
            if cooldown and cooldown[0][0] == time:
                _, f, ch = cooldown.popleft()
                heapq.heappush(heap, (f, ch))

            # No character is available to place
            if not heap:
                return ""

            # Use the most frequent available character
            f, ch = heapq.heappop(heap)
            result.append(ch)
            f += 1  # since frequencies are negative

            # Put it into cooldown if it still has remaining occurrences
            if f < 0:
                cooldown.append((time + 2, f, ch))

            time += 1

        return "".join(result)