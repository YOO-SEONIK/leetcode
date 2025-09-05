# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.tree_maker([i for i in range(1, n+1)])
        
    def tree_maker(self, nums):
        if not nums:
            return [None]
        ret = []
        for i, num in enumerate(nums):
            lefts = self.tree_maker(nums[:i])
            rights = self.tree_maker(nums[i+1:])
            temp = []
            for c in range(len(lefts) * len(rights)):
                temp.append(TreeNode(val=num))
            c = 0
            for l in range(len(lefts)):
                for r in range(len(rights)):
                    temp[c].left = lefts[l]
                    temp[c].right = rights[r]
                    c += 1
            ret += temp
        return ret
        