class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l, r = 0, len(nums)-1

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                totalSum = nums[i] + nums[j] + nums[k]
                if totalSum < 0:
                    j += 1
                elif totalSum > 0:
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    if nums[k] == nums[k+1]:
                        k -= 1

        return res

                