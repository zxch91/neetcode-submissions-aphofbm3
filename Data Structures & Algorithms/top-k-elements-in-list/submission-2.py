class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)

        for key, val in counter.items():
            bucket[val].append(key)

        res = []

        for i in range(len(bucket)- 1, 0, -1):
            for num in bucket[i]:
                if len(res) < k:
                    res.append(num)
        return res