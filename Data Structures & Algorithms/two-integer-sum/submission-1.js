class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
      let index = 0
      let isLastNum = true;
      while (isLastNum) {
        if (index > nums.length - 1) {
            isLastNum = true;
            return false;
        }
        let base = nums[index]
        for (let i = index+1; i <= nums.length; i++) {
          
          if (base + nums[i] === target) {
            return [index, i]
          }
        }
        index += 1;
      }
    }
}
