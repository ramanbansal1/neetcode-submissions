from collections import deque 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = [(i, (n, j)) for (n, i, j) in trips]
        heapq.heapify(heap)

        dist = 0
        passengers = 0

        offload = []
        while len(heap) > 0:
            while len(offload) > 0 and heap[0][0] >= offload[0][0]:
                j, n = heapq.heappop(offload)
                dist = j
                passengers -= n
            i, (n, j) = heapq.heappop(heap)
            passengers += n 

            if passengers > capacity:
                return False

            heapq.heappush(offload, (j, n))
            dist = i 

        return True
            