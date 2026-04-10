class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        li=[[] for i in range(len(nums)+1) ]
        print(li)

        for num in nums:
            count[num]=count.get(num,0)+1
        for item,value in count.items():
            li[value].append(item)

        res=[]
        for i in range(len(li)-1,0,-1):
            for n in li[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res


        
            



        