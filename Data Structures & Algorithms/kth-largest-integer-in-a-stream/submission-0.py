class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap.append(val)
            self._sift_up(len(self.heap) - 1)
        elif val > self.heap[0]:
            self.heap[0] = val
            self._sift_down(0)

        return self.heap[0]

    # ---------- heap helpers ----------

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
