class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [];   
        subset = [];

        def dfs(pos):
            if pos >= len(nums):
                res.append(subset.copy());
                return;
            
            # decision to includes nums[pos]
            subset.append(nums[pos]);
            dfs(pos + 1);
            # decision to NOT include nums[pos]
            subset.pop();            
            dfs(pos + 1);

        dfs(0);
        return res;