class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0

        for i in prices:
            if i < lowest:
                lowest = i

            res = max(res, i - lowest)

        return res
