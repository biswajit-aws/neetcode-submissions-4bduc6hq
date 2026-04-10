class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,res=0,len(height)-1,0
        left_max, right_max = height[l], height[r]
        while(l<r):
            if left_max<right_max:
                l+=1
                left_max=max(left_max,height[l])
                res+=max((left_max-height[l]),0)
            else :
                r-=1
                right_max=max(right_max,height[r])
                res+=max((right_max-height[r]),0)
        return res
        