class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        tmp_answer = []
        pre = nums[0]
        tmp = [pre]
        for i in range(1, len(nums)):
            if (pre + 1) == nums[i]:
                pre = nums[i]
                tmp.append(nums[i])
            else:
                tmp_answer.append(tmp)
                pre = nums[i]
                tmp = [pre]
        tmp_answer.append(tmp)
        
        answer = []
        for a in tmp_answer:
            if len(a) == 1:
                answer.append(str(a[0]))
            else:
                answer.append(str(a[0])+"->"+str(a[-1]))

        return answer
        