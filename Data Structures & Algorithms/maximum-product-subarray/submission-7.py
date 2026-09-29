class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # curProd = nums[0];
        # maxProd = curProd;

        # for i in range(1, len(nums)):
        #     curProd = nums[i];
        #     if (curProd <= 0):
        #         continue;
        #     else:
        #         maxProd = max(maxProd, curProd);

        # return maxProd; 
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
