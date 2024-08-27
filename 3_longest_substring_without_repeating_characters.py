class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charset = set()

        for i in range(len(s)):
            if s[i] in charset:
                charset.remove(i)

            charset.add(i)

            l = len(charset)

            res = max(l, res)

        return res

