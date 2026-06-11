# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True

        def dfs(curr):
            if not curr or self.balance == False:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if self.balance:
                if abs(left - right) > 1:
                    self.balance = False
                    return - 10
            return 1 + max(left, right)
        dfs(root)
        return self.balance

