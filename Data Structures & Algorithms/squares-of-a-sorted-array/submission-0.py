class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        pos = len(nums) - 1

        while l <= r:
            s = nums[l]**2
            e = nums[r]**2

            if s < e:
                res[pos] = e
                r -= 1
            else:
                res[pos] = s
                l += 1
            pos -= 1
        return res
            
                
                
                