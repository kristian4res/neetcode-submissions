class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Step 1: Pack pairs into the first half
        for i in range(n):
            nums[i] = (nums[i + n] << 10) | nums[i]
            
        # Step 2: Unpack from the back to avoid overwriting
        for i in range(n - 1, -1, -1):
            y = nums[i] >> 10       # extract the (i + n)-th element
            x = nums[i] & 1023      # extract the i-th element
            
            nums[2 * i + 1] = y
            nums[2 * i] = x
            
        return nums
