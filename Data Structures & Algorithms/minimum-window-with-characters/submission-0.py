class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        tMap,sMap={},{}
        res=""
        min=1000
        for i in range (len(t)):
            tMap[t[i]]=1+tMap.get(t[i],0)
        
        needed=len(tMap)
        having=0
        for right in range(len(s)):
            sMap[s[right]]=1+sMap.get(s[right],0)
            if s[right] in tMap and tMap[s[right]]==sMap[s[right]]:
                having+=1
                while(having==needed):
                    if(right-left+1)<min:
                        res=s[left:right+1]
                        min=right-left+1
                    sMap[s[left]]-=1
                    if s[left] in tMap and sMap[s[left]]<tMap[s[left]]:
                        having-=1
                    left+=1
        return res
                
            






            
            



        