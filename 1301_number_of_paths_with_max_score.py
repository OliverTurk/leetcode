class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        ops = [(0, -1), (-1, 0), (-1, -1)]

        MOD = 10 ** 9 + 7

        M = len(board)
        N = len(board[0])

        dp = [[0] * N for _ in range(M)]
        dpc = [[0] * N for _ in range(M)]


        dpc[M-1][N-1] = 1

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if board[i][j] == "X" or dpc[i][j] == 0:
                    continue

                for di, dj in ops:
                    ni = i + di
                    nj = j + dj

                    delta = 0

                    if board[ni][nj].isnumeric():
                        delta = int(board[ni][nj])

                    if ni >= 0 and ni < M and nj >=0 and nj < N and board[ni][nj] != "X":
                        if dp[i][j] + delta > dp[ni][nj]:
                            dp[ni][nj] = dp[i][j] + delta
                            dpc[ni][nj] = dpc[i][j]
                        elif dp[i][j] + delta == dp[ni][nj]:
                            dpc[ni][nj] += dpc[i][j]
    

        return [dp[0][0], dpc[0][0] % MOD]
