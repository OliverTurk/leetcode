class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        freq = defaultdict(int)

        for n in nums:
            b = -inf
            s = inf

            x = n
            
            while n != 0:
                d = n % 10
                n //= 10

                b = max(b, d)
                s = min(s, d)

            freq[b-s] += x
        
        return freq[max(freq.keys())
