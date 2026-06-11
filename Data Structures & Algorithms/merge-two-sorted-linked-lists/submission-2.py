# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not h1:
            return h2
        if not h2:
            return h1

        if h2.val <= h1.val:
            res = h2
            curr = h2
            h2 = h2.next
        elif h1.val < h2.val:
            res = h1
            curr = h1
            h1 = h1.next
        while h1 != None and h2!= None:
            print(h1.val,h2.val)
            if h1.val < h2.val:
                curr.next = h1
                curr = curr.next
                h1 = h1.next
            else:
                curr.next = h2
                curr = curr.next
                h2 = h2.next
        if h1:
            curr.next = h1
            
        if h2:
            curr.next = h2
            

        return res