# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxval, minval):
            if not node:
                return True

            if node.val <= minval or node.val >= maxval:
                return False
            minval = min(node.val, minval)
            maxval = max(node.val, maxval)
            leftres = dfs(node.left, node.val, minval)
            rightres = dfs(node.right, maxval, node.val)

            return leftres and rightres

        return dfs(root, 1100, -1100)
