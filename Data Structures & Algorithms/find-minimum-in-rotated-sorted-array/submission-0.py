class Solution:
    def findMin(self, nums: List[int]) -> int:
        curMin = nums[0];
        l, r = 0, len(nums) - 1;

        while l <= r:
            if nums[l] < nums[r]:
                curMin = min(curMin, nums[l]);
                break;

            mid = (l + r) // 2;
            curMin = min(curMin, nums[mid]);
            if nums[mid] >= nums[l]:
                l = mid + 1;
            else:
                r = mid - 1;
        return curMin;
