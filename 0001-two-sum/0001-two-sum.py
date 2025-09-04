class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}
        
        for i, num in enumerate(nums):
            aim = target - num
            
            if aim in nums_map:
                return [nums_map[aim], i]

            nums_map[num] = i
        