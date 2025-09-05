# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:    
            return head
        
        smaller, bigger = ListNode(0), ListNode(0)
        s, b = smaller, bigger
        
        if head.val < x:
            s.next = ListNode(head.val)
            s = s.next
        else:
            b.next = ListNode(head.val)
            b = b.next
        
        while head.next:
            head = head.next
            if head.val < x:
                s.next = ListNode(head.val)
                s = s.next
            else:
                b.next = ListNode(head.val)
                b = b.next
        
        s.next = bigger.next
        return smaller.next
        