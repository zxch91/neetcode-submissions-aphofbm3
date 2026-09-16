class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0:1}

        res = 0
        currSum = 0

        for i, num in enumerate(nums):
            currSum += num

            if currSum-k in dic:
                res += dic[currSum-k]
            dic[currSum] = dic.get(currSum, 0) + 1

        return res