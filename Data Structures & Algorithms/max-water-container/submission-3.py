class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,max_area=0,len(height)-1,0
        while(l<r):
            area=min(height[l],height[r])*(r-l)
            max_area=max(max_area,area)
            if(height[l]<height[r]):
                l+=1
                while height[l]<height[l-1] and l<r:
                    l+=1
            else:
                r-=1
                while height[r]<height[r+1] and l<r:
                    r-=1
        return max_area
            
        