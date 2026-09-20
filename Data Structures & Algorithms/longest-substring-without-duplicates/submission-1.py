class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = set()

        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in dic:
                dic.remove(s[l])
                l+= 1
            dic.add(s[r])

            res = max(res, r-l+1)
        return res