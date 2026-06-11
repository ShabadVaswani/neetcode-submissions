# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        revhead = slow.next
        slow.next = None

        # reversing ll:
        prev, curr = None, revhead
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        revhead = prev
        hd = head
        while revhead :
            tmp = hd.next
            tmp2 = revhead.next
            hd.next = revhead
            revhead.next = tmp
            hd = tmp
            revhead = tmp2







