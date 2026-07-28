class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        freq = Counter(s)

        res = ""

        res += y * freq[y]
        res += x * freq[x]

        for c, n in freq.items():
            if c in (x, y):
                continue

            res += c * n

        return res
