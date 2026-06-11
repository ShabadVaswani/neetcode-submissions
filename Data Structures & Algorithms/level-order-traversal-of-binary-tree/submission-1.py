# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ls = []

        def dfs(curr, level):
            if not curr:
                return 
            while len(self.ls) <= level:
                self.ls.append([])
            self.ls[level].append(curr.val)
            dfs(curr.left, level+1)
            dfs(curr.right, level+1)
            return
        dfs(root, 0)
        return self.ls