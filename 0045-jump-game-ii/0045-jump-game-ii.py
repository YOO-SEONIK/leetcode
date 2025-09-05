class Solution:
    def jump(self, nums: List[int]) -> int:
        max_num = 0
        max_jump = 0
        jump = 0

        for i in range(len(nums)-1):
            max_num = max(max_num, i+nums[i])
            if max_num >= len(nums)-1:
                jump +=1
                break
            
            if i == max_jump:
                jump+=1
                max_jump = max_num
        return jump
        
        
        