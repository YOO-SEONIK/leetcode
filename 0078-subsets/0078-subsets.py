class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx,arr):
            ret.append(arr[:])
            for i in range(idx, len(nums)):
                dfs(i+1, arr + [nums[i]])

        ret = []
        dfs(0, [])

        return ret        
        