class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        result = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result if result is not None else len(nums)
        