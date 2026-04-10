# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.good=0
        def dfs(node,max):
            if node:
                if node.val>=max:
                    max=node.val
                    self.good=self.good+1
                dfs(node.left,max)
                dfs(node.right,max)
        dfs(root,-100)
        return self.good


        