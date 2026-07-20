class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        N = len(cost)

        cost.sort(reverse=True)

        res = 0

        for i in range(0, N, 3):
            res += cost[i]

            if i + 1 < N:
                res += cost[i+1]

        return re
