class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(prefix, num):
            if not num:
                if prefix not in answer:
                    answer.append(prefix)
                return

            for i, n in enumerate(num):
                dfs(prefix + [n], num[:i] + num[i+1:])

        dfs([], nums)
    
        return answer
        