class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        best = 0
        res = 0

        for i in range(N):
            res = max(res, best + values[i] - i)
            best = max(best, values[i] + i)

        return res
