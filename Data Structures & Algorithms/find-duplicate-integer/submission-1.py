class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset=set()
        for val in nums:
            if not val in hashset:
                hashset.add(val)
            else:
                return val
        return -1



        