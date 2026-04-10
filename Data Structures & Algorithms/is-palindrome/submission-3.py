class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        final_str=""
        for ch in s:
            if(ch.isalnum()):
                final_str+=ch
        i=0;
        j=len(final_str)
        while(i<j-1-i):
            if final_str[i]!=final_str[j-1-i]:
                return False
            else:
                i+=1
        return True
        