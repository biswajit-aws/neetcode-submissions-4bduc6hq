class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=len(s1)
        while(right<len(s2)+1):
            li =[0]*26
            sub=s2[left:right]
            print(sub)
            for i in range(len(s1)):
                li[ord(s1[i])-ord('a')]+=1
                li[ord(sub[i])-ord('a')]-=1
            for i in range (len(li)):
                if li[i]!=0:
                    left+=1
                    right+=1
                    break
                elif i==25 and li[i]==0:
                    return True
        return False

            

                




            
            
        