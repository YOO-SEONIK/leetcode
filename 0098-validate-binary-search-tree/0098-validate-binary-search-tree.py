# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, small, big):
            if not root:
                return True
            
            if not small < root.val < big:
                return False
            
            return check(root.left, small, root.val) and check(root.right, root.val, big)
        
        return check(root, -inf, inf)
        