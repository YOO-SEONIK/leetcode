from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []
        q = deque()
        q.append((root, 0))
        while q:
            cur_node, cur_level = q.popleft()
            if len(ret) == cur_level:
                ret.append([cur_node.val])
            else:
                ret[cur_level].append(cur_node.val)
            if cur_node.left != None:
                q.append((cur_node.left, cur_level+1))
            if cur_node.right != None:
                q.append((cur_node.right, cur_level+1))
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i].reverse()
        return ret