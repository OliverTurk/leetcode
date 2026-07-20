class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""

        for i in range(len(number)):
            if number[i] == digit:
                best = max(best, number[:i] + number[i+1:])
        
        return best
