class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)

        res = 0

        cur = defaultdict(int)

        l = 0

        for r in range(N):
            cur[s[r]] += 1

            while len(cur) == 3:
                res += (N - r)
                
                cur[s[l]] -= 1

                if cur[s[l]] == 0:
                    del cur[s[l]]
                
                l += 1

        return res
