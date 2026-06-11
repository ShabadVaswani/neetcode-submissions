# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        level = 1
        s = [[root,1]]
        flag = False
        while s:
                x = s.pop()
                if x[0].right:
                    s.append([x[0].right, x[1]+1])
                    level = max(level, x[1]+1)
                if x[0].left:
                    s.append([x[0].left, x[1]+1])
                    level = max(level, x[1]+1)
                

        return level