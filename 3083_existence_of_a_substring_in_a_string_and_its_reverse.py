class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)

        reverse = s[::-1]
        
        substrings = set()

        for i in range(N):
            for j in range(i+2, N+1):
                substrings.add(reverse[i:j])

        for i in range(N):
            for j in range(i+2, N+1):
                if s[i:j] in substrings:
                    return True

        return False
