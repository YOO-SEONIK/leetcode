# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        values = []
        cur = head
        while cur != None:
            values.append(cur.val)
            cur = cur.next
        return self.tree_builder(values)
            
    def tree_builder(self, values):
        if not values:
            return None
        
        if len(values) == 1:
            return TreeNode(val=values[0])
        
        mid_idx = len(values) // 2
        mid_value = values[mid_idx]
        head = TreeNode(val=mid_value)
        
        head.left = self.tree_builder(values[:mid_idx])
        head.right = self.tree_builder(values[mid_idx+1:])
        
        return head
        