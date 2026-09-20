class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, arr):
            if sum(arr) == target:
                res.append(arr[:])
                return
            if sum(arr) > target or i >= len(nums):
                return
            
            arr.append(nums[i])
            dfs(i,arr)
            arr.pop()
            dfs(i+1,arr)

        dfs(0,[])
        return res