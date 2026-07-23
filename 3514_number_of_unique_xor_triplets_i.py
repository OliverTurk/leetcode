class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 2:
            return N

        length = 0

        while N:
            length += 1
            N >>= 1
        
        return 2 ** length
