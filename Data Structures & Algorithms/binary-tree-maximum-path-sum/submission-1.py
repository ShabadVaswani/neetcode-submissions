# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxsum = float("-inf")
        def dfs(curr):
            if not curr:
                return 0

            sumleft = dfs(curr.left)
            sumleft = sumleft if sumleft>0 else 0
            sumright = dfs(curr.right)
            sumright = sumright if sumright>0 else 0
            sumcurrinpath = sumleft + sumright + curr.val
            if sumcurrinpath > self.maxsum:
                self.maxsum = sumcurrinpath
            sumoneway = curr.val + max(sumleft, sumright)

            return sumoneway

        dfs(root)

        return self.maxsum

        