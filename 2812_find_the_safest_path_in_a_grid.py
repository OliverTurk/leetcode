class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves = []

        N = len(grid)
        M = len(grid[0])

        distances = [[inf] * M for _ in range(N)]
        q = deque()

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    thieves.append((i, j))
                    distances[i][j] = 0
                    q.append((i,j))

        ops = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            x, y = q.popleft()

            for dx, dy in ops:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < N and ny >=0 and ny < M and distances[nx][ny] == inf:
                    distances[nx][ny] = distances[x][y] + 1
                    q.append((nx, ny))

        def good(v):
            seen = set()

            q = deque()
            q.append((0,0))
            
            while q:
                x, y = q.popleft()

                if (x, y) in seen:
                    continue
                    
                seen.add((x, y))

                if distances[x][y] < v:
                    return False

                if x == N - 1 and y == M - 1:
                    return True

                for dx, dy in ops:
                    nx = x + dx
                    ny = y + dy

                    if nx >= 0 and nx < N and ny >=0 and ny < M and (nx, ny) not in seen and distances[nx][ny] >= v:
                        q.append((nx, ny))

            return False

        l = 0
        r = M + N

        while l < r:
            m = (l + r + 1) // 2

            if good(m):
                l = m
            else:
                r = m - 1

        return l

