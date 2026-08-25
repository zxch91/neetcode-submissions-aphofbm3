class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in dic:
                return [dic[remainder], i]
            else:
                dic[n] = i
