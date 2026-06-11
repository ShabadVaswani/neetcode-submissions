# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeList(self, h1, h2):
        dummy = ListNode(0)
        tail = dummy
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2=h2.next
            tail=tail.next
        tail.next = h1 if h1 else h2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        q = deque(lists)


        while True:
            if len(q) == 1:
                break
            q.append(self.mergeList(q.popleft(), q.popleft()))

            
            
        return q.popleft()






        