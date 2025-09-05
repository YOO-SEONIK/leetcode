class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums[0] == target:   return True
        
        for n in range(1, len(nums)):
            if nums[n] == target:
                return True
            elif nums[n-1] < target < nums[n]:
                return False
        
        return False
        