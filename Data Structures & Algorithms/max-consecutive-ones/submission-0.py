class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
                maxOne = max(length, maxOne)
            else:
                length = 0

        return maxOne