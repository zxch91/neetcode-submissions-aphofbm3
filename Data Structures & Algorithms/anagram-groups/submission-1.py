class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for char in word:
                value = ord(char) - ord('a')
                chars[value] += 1
            dic[tuple(chars)].append(word)
        
        return list(dic.values())