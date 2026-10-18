class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases: negatives and numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        # Process until we reach the middle
        while x > rev:
            rev = (rev * 10) + (x % 10)
            x //= 10

        # For even length: x == rev
        # For odd length:  x == rev // 10 (discards middle digit)
        return x == rev or x == rev // 10