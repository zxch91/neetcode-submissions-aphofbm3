class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            prereq[course].append(pre)

        visited = set()
        done = set()
        order = []
        def dfs(crs):
            if crs in visited:
                return False
            if crs in done:
                return True

            visited.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            done.add(crs)
            order.append(crs)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []

        return order
            
