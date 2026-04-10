class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #key value pair
        stack=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                stack_t,stack_idx=stack.pop()
                res[stack_idx]=i-stack_idx
            stack.append([temp,i])
        return res
            

        