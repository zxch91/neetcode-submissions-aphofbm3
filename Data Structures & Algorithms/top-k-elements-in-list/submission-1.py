class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)

        for num, count in counter.items():
            arr[count].append(num)

        res = []

        for i in range(len(arr))[::-1]:
            for num in arr[i]:
                if len(res) < k:
                    res.append(num)
        return res
        
