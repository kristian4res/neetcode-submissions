# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if (node.left and not node.right):
                result.append(node.left.val)
            if (not node.left and node.right):
                result.append(node.right.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return result
