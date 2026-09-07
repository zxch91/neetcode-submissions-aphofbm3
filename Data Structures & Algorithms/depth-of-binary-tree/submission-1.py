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

        q = deque()
        res = 0

        q.append([root,1])

        while q:
            node,val = q.popleft()
            res = max(res,val)
            if node.left:
                q.append([node.left,val+1])
            if node.right:
                q.append([node.right,val+1])
        return res
        