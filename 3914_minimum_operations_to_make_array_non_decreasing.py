class Solution:
    def minOperations(self, nums: list[int]) -> int:
        biggest = nums[0]

        res = 0
        for n in nums:
            n += res
            biggest = max(biggest, n)
            res += biggest - n

        return res
