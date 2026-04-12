class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dic = defaultdict()

        for num in nums:
            if num in dic:
                return True
            dic[num] = True
        return False
