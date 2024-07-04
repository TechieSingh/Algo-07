# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  
        result = dummy
        su = 0
        current = head.next  

        while current:
            if current.val == 0:
                result.next = ListNode(su)
                result = result.next
                su = 0
            else:
                su += current.val
            current = current.next

        return dummy.next
        