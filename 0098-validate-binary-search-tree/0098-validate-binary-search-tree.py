class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, small, big):
            if not root:
                return True
            
            if not small < root.val < big:
                return False
            
            return check(root.left, small, root.val) and check(root.right, root.val, big)
        
        return check(root, -inf, inf)