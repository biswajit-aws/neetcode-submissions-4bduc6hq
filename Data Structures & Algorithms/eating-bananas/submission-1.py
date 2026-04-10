class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        res=0
        while left<=right:
            rate=left+((right-left)//2)
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/rate)
            if hours<=h:
                res=rate
                right=rate-1
            elif hours>h:
                left=rate+1
        return res 
            



        