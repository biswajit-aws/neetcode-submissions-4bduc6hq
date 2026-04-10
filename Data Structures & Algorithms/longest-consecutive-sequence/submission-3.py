class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
    
        for num in nums:
            curr=1
            i=1
            while num+i in nums:
                curr=curr+1
                i=i+1
            if(curr>longest):
                longest=curr

        return longest

            
                


        