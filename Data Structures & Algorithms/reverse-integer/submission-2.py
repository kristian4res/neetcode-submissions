class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)

        # Magnitude limit depends on sign: 2^31-1 for positive, 2^31 for negative
        limit = 2**31 - 1 if sign == 1 else 2**31

        res = 0
        while x:
            digit = x % 10
            x //= 10

            # Overflow check BEFORE committing the digit
            if res > limit // 10 or (res == limit // 10 and digit > limit % 10):
                return 0

            res = res * 10 + digit

        return sign * res