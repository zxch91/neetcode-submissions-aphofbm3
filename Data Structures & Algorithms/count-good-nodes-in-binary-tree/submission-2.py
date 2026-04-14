
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        self.res = 0

        def dfs(self, node, largest):
            if node.val >= largest:
                self.res += 1
                largest = node.val
            if node.left:
                dfs(self, node.left, largest)
            if node.right:
                dfs(self, node.right, largest)
        
        dfs(self, root, root.val)
        return self.res
