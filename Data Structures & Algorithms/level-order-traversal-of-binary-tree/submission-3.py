# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.ls = [[]]

        q = collections.deque()
        q.append(root)
        qleft = 1
        level = 0
        while q:
            if qleft == 0:
                self.ls.append([])
                level+=1
                qleft = len(q)
            qleft-=1
            curr = q.popleft()
            self.ls[level].append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return self.ls