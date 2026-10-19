class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            count = 0;
            temp = i
            for _ in range(32):
                count += (temp & 1);
                temp = temp >> 1;
            output.append(count)
        return output