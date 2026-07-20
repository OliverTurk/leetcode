class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        @cache
        def f(i, j):
            if i == M:
                return 0

            best = matrix[i][j] +  min(
                f(i+1, j),
                f(i+1, j-1) if j > 0 else inf,
                f(i+1, j+1) if j < N - 1 else inf
            )

            return best

        res = inf
        for j in range(N):
            res = min(res, f(0, j))
        
        return res

