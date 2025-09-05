class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_result = set(range(1,len(nums)+1))
        set_nums = set(nums)
        return list(set_result-set_nums)
        