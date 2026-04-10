class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        res=0
        count_map={}
        for right in range(len(s)):
            count_map[s[right]]=1+count_map.get(s[right],0)
            while right-left+1-max(count_map.values())>k:
                count_map[s[left]]-=1
                left=left+1
            res=max(res,right-left+1)

        return res
        





        