class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            li=[0]*26
            for c in s:
                li[ord(c)-ord('a')]+=1
            res[tuple(li)].append(s)

        return list(res.values())


            
        