class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(capital_heap)

        
        profit_heap = []
        counter = 0
        while counter < k:
            while capital_heap and capital_heap[0][0] <= w:
                c, p = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, (-p, c))
                
            if not profit_heap:
                break
            
            p, c = heapq.heappop(profit_heap)
            w = w - p
            counter += 1
        return w