class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, arr, total):
            if total == target:
                res.append(arr[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                arr.append(candidates[i])
                dfs(i + 1, arr, total + candidates[i])
                arr.pop()

        dfs(0, [], 0)
        return res