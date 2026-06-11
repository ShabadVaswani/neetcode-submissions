# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorder = []
        def dfs(curr):
            if not curr:
                self.preorder.append("N")
                return 
            self.preorder.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
            return
        dfs(root)
        return ",".join(self.preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        self.preorderq = collections.deque(preorder)
        self.index = 0
        print(preorder)

        def dfs():
            top = self.preorderq.popleft()
            if top == 'N':
                return None
            node = TreeNode(top)
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
