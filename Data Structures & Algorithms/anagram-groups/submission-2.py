class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for c in s:
                value = ord(c) - ord('a')
                word[value] += 1
            res[tuple(word)].append(s)
        
        return list(res.values())