class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        # XOR all characters in s
        for c in s:
            res ^= ord(c)
            
        # XOR all characters in t
        for c in t:
            res ^= ord(c)
            
        # The remaining value is the ASCII code of the extra character
        return chr(res)