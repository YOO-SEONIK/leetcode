class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[count] in nums[:count]:
                del nums[count]
                count -=1
            count += 1