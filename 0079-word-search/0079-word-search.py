class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        stack = []
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(y: int, x: int, depth: int):
            if depth == len(word):
                return True

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == word[depth]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = 1
                        if dfs(ny, nx, depth + 1):
                            return True
                        visited[ny][nx] = 0

            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    visited[y][x] = 1
                    if dfs(y, x, 1):
                        return True
                    visited[y][x] = 0

        return False
        