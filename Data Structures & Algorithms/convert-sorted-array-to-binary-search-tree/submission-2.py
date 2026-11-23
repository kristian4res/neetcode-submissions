class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # 2. Pick the middle element as the root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # 3. Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        # Initial call covers the entire array
        return build(0, len(nums) - 1)
