class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            rob1, rob2 = 0, 0

            for num in houses:
                temp = rob1
                rob1 = max(rob1, rob2 + num)
                rob2 = temp

            return rob1

        return max(
            rob_line(nums[:-1]),  # don't rob last house
            rob_line(nums[1:])    # don't rob first house
        )