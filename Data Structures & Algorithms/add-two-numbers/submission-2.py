# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2=0,0
        base1,base2=0,0
        while l1:
            num1=num1+(l1.val)*(10**base1)
            l1=l1.next
            base1+=1

        while l2:
            num2=num2+(l2.val)*(10**base2)
            base2+=1
            l2=l2.next
        dummy=ListNode(0)
        total=num1+num2
        if total==0:
            return dummy
        head=dummy
        while total/10 >0:
            curr=ListNode(total%10)
            dummy.next=curr
            dummy=dummy.next
            total=total//10
        return head.next



        