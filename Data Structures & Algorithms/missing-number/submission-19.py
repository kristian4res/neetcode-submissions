from collections import defaultdict;

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # numSet = set(n for n in range(0, len(nums)+1));
        
        # for num in numSet:
        #     if num not in nums:
        #         return num;
        if (0 not in nums):
            return 0;

        maxNum = len(nums);
        for num in nums:
            l, r = num - 1, num + 1;
            if (l not in nums and l >= 0):
                return l;
            if (r not in nums and r <= maxNum):
                return r;
        
        