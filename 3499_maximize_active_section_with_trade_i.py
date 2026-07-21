class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        N = len(s)
        ones = s.count("1")
        
        res = ones
        cur = prev = 0

        for i in range(N):
            if s[i] == "0":
                cur += 1
            elif cur:
                if prev:
                    res = max(res, ones + cur + prev)
                prev, cur = cur, 0

        if cur and prev:
            res = max(res, ones + cur + prev)

        return res
       
