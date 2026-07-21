class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = [0] * 10

        bulls = cows = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                if count[int(s)] < 0: cows += 1
                if count[int(g)] > 0: cows += 1

            count[int(s)] += 1
            count[int(g)] -= 1

        return f"{bulls}A{cows}B"
