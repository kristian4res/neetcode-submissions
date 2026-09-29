from collections import defaultdict;

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if (0 not in nums):
            return 0;

        for num in nums:
            l, r = num - 1, num + 1;
            if (l not in nums and l >= 0):
                return l;
            if (r not in nums and r <= len(nums)):
                return r;
        
        