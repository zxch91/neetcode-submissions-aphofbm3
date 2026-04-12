class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = defaultdict()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in dic:
                dic.pop(s[l])
                l += 1
            dic[s[r]] = True
            
            res = max(res, r-l+1)
        return res 


        