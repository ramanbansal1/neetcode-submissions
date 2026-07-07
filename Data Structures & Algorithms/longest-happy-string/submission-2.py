import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))

        result = []

        while heap:
            freq1, char1 = heapq.heappop(heap)

            # Would adding char1 create three consecutive characters?
            if len(result) >= 2 and result[-1] == result[-2] == char1:

                # No alternative exists
                if not heap:
                    break

                # Use the second most frequent character
                freq2, char2 = heapq.heappop(heap)

                result.append(char2)
                freq2 += 1  # since frequencies are negative

                if freq2 < 0:
                    heapq.heappush(heap, (freq2, char2))

                # Put the first character back
                heapq.heappush(heap, (freq1, char1))

            else:
                result.append(char1)
                freq1 += 1

                if freq1 < 0:
                    heapq.heappush(heap, (freq1, char1))

        return "".join(result)