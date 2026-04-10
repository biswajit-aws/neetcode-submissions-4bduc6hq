class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # hashmap={}
      # for i,n in enumerate(nums):
      #    diff=target-n
      #    if diff in hashmap:
      #       return [hashmap[diff],i]
      #    else:
      #       hashmap[n]=i
      # return []
      li=[]
      for i,n in enumerate(nums):
         li.append([n,i])
      li.sort()

      i,j=0,len(nums)-1

      while i<j:
         curr=li[i][0]+li[j][0]
         if curr==target:
            return [min(li[i][1],li[j][1]),max(li[i][1],li[j][1])]
         if curr<target:
            i=i+1
         if curr>target:
            j=j-1
      return []






        