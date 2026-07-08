import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # Rooms that are free (min room index)
        available = list(range(n))
        heapq.heapify(available)

        # Rooms that are busy: (free_time, room_index)
        busy = []

        # Number of meetings held by each room
        used = [0] * n

        for start, end in meetings:

            # Free every room that has become available
            while busy and busy[0][0] <= start:
                free_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                room = heapq.heappop(available)
                used[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                free_time, room = heapq.heappop(busy)
                used[room] += 1
                heapq.heappush(busy, (free_time + duration, room))

        ans = 0
        for i in range(1, n):
            if used[i] > used[ans]:
                ans = i

        return ans