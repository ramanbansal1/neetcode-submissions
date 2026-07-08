class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:

        if len(self.first_half) > 0 and -self.first_half[0] > num:
            heapq.heappush(self.first_half, -num)
        
        else:
            heapq.heappush(self.second_half, num)

        while len(self.first_half) > len(self.second_half):
            i = -heapq.heappop(self.first_half) 
            heapq.heappush(self.second_half, i)

        while len(self.first_half) < len(self.second_half):
            i = heapq.heappop(self.second_half) 
            heapq.heappush(self.first_half, -i)

    def findMedian(self) -> float:
        print(self.first_half, self.second_half)
        if len(self.first_half) == len(self.second_half):
            return .5 * (-self.first_half[0] + self.second_half[0])

        if len(self.first_half) > len(self.second_half):
            return - self.first_half[0]

        
        if len(self.first_half) < len(self.second_half):
            return self.second_half[0]
