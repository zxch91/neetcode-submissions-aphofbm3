class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n-1 != len(edges):
            return False
        nodes = {i: [] for i in range(n)}

        for parent, child in edges:
            nodes[parent].append(child)
            nodes[child].append(parent)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  

            visited.add(node)

            for nei in nodes[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
        