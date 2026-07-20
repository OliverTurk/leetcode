class Solution:
    def canAliceWin(self, n: int) -> bool:
        p2 = False
        x = 10

        while n >= x and x > 0:
            n -= x
            p2 = not p2
            x -= 1

        return p2
