class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)) or max(nums) - min(nums) + 1 != len(nums):
            return False
        return True
