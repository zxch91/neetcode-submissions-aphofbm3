class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic = {}
        res = 0

        l = 0
        freq = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r],0)
            freq = max(freq, dic[s[r]])

            while (r-l+1) - freq > k:
                dic[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        return res