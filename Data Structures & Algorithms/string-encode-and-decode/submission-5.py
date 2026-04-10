class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded :str = ""
        for s in strs:
            encoded += str(len(s)) + "@" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        list=[]
        if s=="":
            return []

        count=""
        i=0
        while i< len(s):
            if s[i] !='@':
                count=count+s[i]
                i=i+1
            else :
                list.append(s[i+1:i+1+int(count)])
                i=i+1+int(count)
                count=""
        return list
            
        





