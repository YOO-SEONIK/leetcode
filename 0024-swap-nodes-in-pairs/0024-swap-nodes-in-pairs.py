# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_lst = []

        while head :
            temp_lst.append(head.val)
            head = head.next

        check_lst = []

        for index in range(0, (len(temp_lst))//2):
            check_lst.append(temp_lst[(2 * index) +1])
            check_lst.append(temp_lst[(2 * index)])

        # ODD CASE
        if len(temp_lst)%2 == 1:
            check_lst.append(temp_lst[-1])

        check_lst = check_lst[::-1]
        final = None
        for value in check_lst:
            final = ListNode(value, final)

        return final
        