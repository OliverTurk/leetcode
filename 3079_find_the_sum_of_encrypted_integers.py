class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        def max_digit(n):
            return max(list(n))

        res = 0

        for n in nums:
            res += int(max_digit(str(n)) * len(str(n)))
        
        return res
