# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        q=collections.deque()
        q.append(root)
        res=[]
        while q:
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if node:
                    if i==length-1:
                        res.append(node.val)
                    print(node.val)
                    left=node.left
                    if left:
                        q.append(left)
                    right=node.right
                    if right:
                        q.append(right)
        return res

            
                
                
        