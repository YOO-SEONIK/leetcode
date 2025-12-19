class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        N, M = len(matrix), len(matrix[0])
        visited = [[0 for _ in range(M)] for y in range(N)]

        x, y, d = 0, 0, 1
        visited[0][0] = 1
        answer = [matrix[0][0], ]

        while True:
            if len(answer) == N*M:
                break
            
            nx = x + dv[d][0]
            ny = y + dv[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 1:
                d = (d+1) % 4
                continue
            
            answer.append(matrix[nx][ny])
            visited[nx][ny] = 1
            x, y = nx, ny
            
        return answer
        