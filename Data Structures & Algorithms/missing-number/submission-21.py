from collections import defaultdict;

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsPresent = set(nums); 

        for i in range(len(nums) + 1):
            if i not in numsPresent:
                return i
        