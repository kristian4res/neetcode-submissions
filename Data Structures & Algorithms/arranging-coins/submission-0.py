class Solution:
    def arrangeCoins(self, n: int) -> int:
        itr = 1
        rows = 0

        while n >= itr:
            rows += 1
            n -= (1 * itr)
            itr += 1
        return rows