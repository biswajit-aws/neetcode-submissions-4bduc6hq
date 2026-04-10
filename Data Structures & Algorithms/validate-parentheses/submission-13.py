class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        map={'(':')','{':'}','[':']'}
        for ch in s:
            if(ch=='('  or ch=='{' or ch =='['):
                li.append(map.get(ch))
            else :
                if(len(li)==0):
                    return False
                else:
                    comp=li.pop(len(li)-1)
                    print(comp)
                    if(comp!=ch):
                        return False

        if(len(li))==0:
            return True
        else:
            return False
        


            
        