class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[-float("infinity")]*(len(nums)-k+1)
        map=dict()
        for i in range(k):
            map[nums[i]]=1+map.get(nums[i],0)
        res[0]=max(map.keys())
        for i in range (k,len(nums)):
            map[nums[i-k]]=map[nums[i-k]]-1
            if(map[nums[i-k]]==0):
                map.pop(nums[i-k])
            map[nums[i]]=1+map.get(nums[i],0)
            res[i-k+1]=max(map.keys())
        return res




        
            

        