# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        def dfs(node, d):
            if not node: return
            if d == len(res): res.append([])
            res[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        res.reverse()
        return res
        