class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
                max_depth = max(depth, max_depth)
            elif s[i] == ")":
                depth -= 1
            else:
                max_depth = max(depth, max_depth)
        
        return max_depth;

        