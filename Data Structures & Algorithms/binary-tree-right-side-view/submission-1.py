# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            res.append(q[-1].val)
            for i in range(qlen):
                node = q.popleft()
                if node: 
                    if node.left: 
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)


        return res


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        return res
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            resmini = []
            for i in range(qlen):
                node = q.popleft()
                if node: 
                    resmini.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if not resmini:
                res.append(resmini)

        return res