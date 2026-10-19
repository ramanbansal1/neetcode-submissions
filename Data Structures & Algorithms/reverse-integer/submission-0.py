class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            result = result * 10 + digit

            if result > INT_MAX:
                return 0

        return sign * result