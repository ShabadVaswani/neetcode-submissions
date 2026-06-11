# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        heady = l1
        n1 = ""
        while heady:
            n1 =  str(heady.val) + n1
            heady = heady.next

        heady = l2
        n2 = ""
        while heady:
            n2 = str(heady.val) + n2
            heady = heady.next
        
        result = int(n1) + int(n2)
        result = str(result)[::-1]
        oldNode = ListNode(int(result[0]), None)
        head = oldNode
        for i in range(len(result)-1): 
            nextNode = ListNode(int(result[i+1]), None)
            oldNode.next = nextNode
            oldNode = nextNode

        return head
