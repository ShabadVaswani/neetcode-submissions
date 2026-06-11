# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        li = []
        st = []
        def dfs(node, l, stack):
            if not node:
                return l
            
            stack.append(node)

            l = dfs(node.left, l, stack)

            l.append(node)
            stack.pop()
            l = dfs(node.right, l, stack)
            return l

        return dfs(root, li, st)[k-1].val
            

           
