from collections import defaultdict;

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if (nums[0] != 0):
        #     return 0;

        # prevNum = nums[0];

        # for num in nums[1:]:
        #     if (num != prevNum + 1):
        #         return prevNum + 1;
        #     prevNum = num;
        # return prevNum;

        numSet = set(n for n in range(0, len(nums)+1));
        print(numSet)
        
        for num in numSet:
            if num not in nums:
                return num;
        
        