# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest = root

        def dfs(curr):
            if not curr:
                return 

            if p.val <= curr.val and q.val >= curr.val or p.val >= curr.val and q.val <= curr.val:
                self.lowest = curr
                return
            if p.val < curr.val and q.val < curr.val:
                dfs(curr.left)

            if p.val > curr.val and q.val > curr.val:
                dfs(curr.right)

        dfs(root)

        return self.lowest

            