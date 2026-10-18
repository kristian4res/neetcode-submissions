class Solution:
    def isPalindrome(self, x: int) -> bool:
        numString = str(x)
        l, r = 0, len(numString) - 1

        while l < r:
            if numString[l] != numString[r]:
                return False
            
            l += 1
            r -= 1

        return True
        