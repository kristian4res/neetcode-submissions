class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if (nums.length === 0) {
            return false;
        }

        let map = {};

        for (let i=0;i<=nums.length;i++) {
            if (map[nums[i]] === 1) {
                return true;
            }
            map[nums[i]] = 1
        }
        return false;
    }
}
