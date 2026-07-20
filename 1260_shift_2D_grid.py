class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])

        k %= (M * N)

        new_grid = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                index = (i * N) + j
                new_index = (index + k) % (M*N)
                ni, nj = new_index // N, new_index % N
                new_grid[ni][nj] = grid[i][j]

        return new_grid
