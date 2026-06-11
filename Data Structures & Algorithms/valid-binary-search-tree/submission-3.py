# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def dfs(curr, gt, lt):
            if not curr:
                return 
            print(gt, curr.val, lt)
            if not(curr.val < lt and curr.val > gt):
                self.valid = False

            dfs(curr.left, gt, min(curr.val, lt))
            dfs(curr.right, max(gt, curr.val), lt)


        dfs(root, float('-inf'), float('inf'))

        return self.valid
