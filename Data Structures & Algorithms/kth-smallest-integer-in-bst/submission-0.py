# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0

        
        tree = deque()

        def dfs(node):
            if node.left:
                dfs(node.left)
            tree.append(node.val)
            if node.right:
                dfs(node.right)
        
        dfs(root)

        while k > 0:
            res = tree.popleft()
            k -= 1
        return res
            
        