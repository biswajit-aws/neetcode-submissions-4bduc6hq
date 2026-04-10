class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_array=[0]*26
        s2_array=[0]*26

        if(len(s1)>len(s2)):
            return False

        for i in range(len(s1)):
            s1_array[ord(s1[i])-ord('a')]+=1
            s2_array[ord(s2[i])-ord('a')]+=1
        
        matches=0
        for i in range(26):
            matches+=(1 if s1_array[i]==s2_array[i] else 0)
        print(matches)
        if matches==26:
                return True

        left=0
        for right in range(len(s1),len(s2)):
            s2_array[ord(s2[right])-ord('a')]+=1

            if s2_array[ord(s2[right])-ord('a')]==s1_array[ord(s2[right])-ord('a')]:
                matches+=1
            elif s2_array[ord(s2[right])-ord('a')]==s1_array[ord(s2[right])-ord('a')]+1:
                matches-=1
            
            s2_array[ord(s2[left])-ord('a')]-=1
            if s2_array[ord(s2[left])-ord('a')]==s1_array[ord(s2[left])-ord('a')]:
                matches+=1
            elif s2_array[ord(s2[right])-ord('a')]==s1_array[ord(s2[left])-ord('a')]-1:
                matches-=1
            if matches==26:
                return True
            left+=1


        return False




            

                




            
            
        