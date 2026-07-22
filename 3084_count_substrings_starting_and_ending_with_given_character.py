class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        N = len(s)
        count = 0

        for i in range(N):
            if s[i] == c:
                count += 1
    
        return count * (count + 1) // 2
