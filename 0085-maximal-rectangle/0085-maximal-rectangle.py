class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols  # 현재 행의 높이
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h: #스택을 사용해 이전보다 작은 높이가 나오면 pop하며 직사각형 넓이 계산
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            return max_area


        for i in range(rows):
            for j in range(cols):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0 # 0이면 0으로 갱신
            
            max_area = max(max_area, largestRectangleArea(height)) #현재 행에서의 최대 넓이 구하고 최대값 갱신

        return max_area
        