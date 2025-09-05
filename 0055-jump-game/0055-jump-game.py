class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums)-2
        reach = len(nums)-1
        
        while(idx >= 0):
            if(nums[idx] + idx >= reach):
                reach = idx
            idx -= 1
            
        return reach == 0
        