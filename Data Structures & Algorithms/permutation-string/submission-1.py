class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic = defaultdict()

        l = 0

        counter1 = Counter(s1)
        counter2 = Counter()
        for r in range(len(s2)):
            counter2[s2[r]] += 1
            while r-l+1 > len(s1):
                counter2[s2[l]] -= 1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                l += 1
            if counter1 == counter2:
                return True
        return False