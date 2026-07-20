class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        is_on = [False] * 101

        for x in bulbs:
            is_on[x] ^= 1

        res = []
        for i in range(101):
            if is_on[i]:
                res.append(i)

        return res
