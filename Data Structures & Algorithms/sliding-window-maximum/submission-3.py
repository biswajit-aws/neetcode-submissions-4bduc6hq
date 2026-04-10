class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[-float("infinity")]*(len(nums)-k+1)
        map=dict()
        prev_max=-float("infinity")
        
        for i in range(k):
            map[nums[i]]=1+map.get(nums[i],0)
        res[0]=max(map.keys())
        prev_max=res[0]
        for i in range (k,len(nums)):
            map[nums[i-k]]=map[nums[i-k]]-1
            if(map[nums[i-k]]==0):
                map.pop(nums[i-k])
                if len(map)>0:
                    prev_max=max(map.keys())
                else :
                    prev_max=-float("infinity")
            map[nums[i]]=1+map.get(nums[i],0)
            res[i-k+1]=max(prev_max,nums[i])
            prev_max=res[i-k+1]
        return res




        
            

        