# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        u = newHead
        v = head

        while n > 0 and v != None:
            v = v.next
            n-=1

        while v != None:
            u = u.next
            v = v.next
        print(u.val)
        u.next = u.next.next

        if u.val==0: return u.next
        return head