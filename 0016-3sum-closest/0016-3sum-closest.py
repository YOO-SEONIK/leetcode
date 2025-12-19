class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best_s = 100000
        
        nums.sort()
        
        for i in range(0, len(nums)-2):
            
            if nums[i] == nums[i-1] and i > 0:
                continue
                
            lower = i + 1
            upper = len(nums) - 1
            
            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                
                if s == target:
                    return s
                
                if abs(target - s) < abs(target - best_s):
                    best_s = s
                    
                if s <= target:
                    lower += 1
                    
                    while nums[lower] == nums[lower - 1] and lower < upper:
                        lower += 1
                
                else:
                    upper -= 1
                
        return best_s
        