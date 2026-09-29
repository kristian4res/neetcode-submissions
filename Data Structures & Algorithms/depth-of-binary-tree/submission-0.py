from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxDepth = 0;
        # queue = deque([root]);

        # if root == None:
        #     return depth;
        
        # def dfs(node, depth, maxDepth):
        #     if node.left:
        #         depth += 1;
        #         return dfs(node.left, depth, maxDepth);
        #     if node.right:
        #         depth += 1;
        #         return dfs(node.right, depth, maxDepth);
        #     maxDepth = max(maxDepth, depth);
        #     return;

        # while len(queue) > 0:
        #     curNode = queue.popleft();
        #     if curNode.left:
        #         return dfs(curNode.left, 1, maxDepth);
        #     if curNode.right:
        #         return dfs(curNode.right, 1, maxDepth);
        # return maxDepth;
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



