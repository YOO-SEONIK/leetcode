from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.prev = None
        self.count = 0
        self.max_count = 0
        self.result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # 현재 노드 처리
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
                self.prev = node.val

            # 최대 빈도 갱신
            if self.count > self.max_count:
                self.max_count = self.count
                self.result = [node.val]
            elif self.count == self.max_count:
                self.result.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.result
        