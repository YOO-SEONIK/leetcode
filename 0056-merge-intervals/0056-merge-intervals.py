class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:(x[0], x[1])) # 정렬하는 부분

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)+1):
            if i == len(intervals):
                result.append([start, end])
                break
            if end < intervals[i][0]: # 겹치지 않는 부분
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else: # 겹치는 부분
                end = max(end, intervals[i][1])
        return result
        