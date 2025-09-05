class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(idx, cur):
            if idx == len(nums):
                ans.append(cur.copy())
                return

            cur.append(nums[idx])
            dfs(idx+1, cur)
            cur.pop()           
            while idx+1 < len(nums) and nums[idx+1] == nums[idx]:
                idx+=1

            
            dfs(idx+1, cur)

        dfs(0, [])
        return ans
        