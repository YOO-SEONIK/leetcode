class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_num = set()

        nums1_set = sorted(set(nums1))
        nums2_set = sorted(set(nums2))

        for num in nums1_set:
            if num in nums2_set:
                intersection_num.add(num)

        return list(intersection_num)
        