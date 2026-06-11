# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        a, b = dummy, head
        c, d = head, head.next
        flag = False
        first = True
        i = k -1
        iterator = b
        reshead = head
        while i:
            iterator = iterator.next
            if iterator == None:
                return dummy.next
            i-=1
        while a and b and not flag:
            print(b.val)
            i = k -1
            while i:
                
                tmp = d.next
                d.next = c
                
                c = d
                d = tmp
                i-=1
                print(i, c.val)
            



            #print(a.val, b.val, c.val)
            a.next = c 
            b.next = d
            a = b
            b = d
            c = b
            if c:
                d = c.next
            else:
                return dummy.next
            #print(a.val, b.val, c.val)
            # checking if elements do exist
            i = k -1
            iterator = b
            while i:
                iterator = iterator.next
                if iterator == None:
                    return dummy.next
                i-=1
        return dummy.next

            





         
        