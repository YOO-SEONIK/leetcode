
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for nlist in lists:
            while nlist:
                arr.append(nlist.val)
                nlist = nlist.next
        
        head = curr = None
        
        for val in sorted(arr):
            if not curr:
                head = curr = ListNode(val)
            else:
                curr.next = ListNode(val)
                curr = curr.next
        
        return head
        