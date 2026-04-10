# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        dummy.next=head
        left,right=dummy,head
        for i in range(n):
            right=right.next 
        while right :
            right=right.next
            left=left.next
        
        temp=left.next.next
        left.next=temp
        return dummy.next
        


        