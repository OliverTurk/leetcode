class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        arr = [x for x in range(1, n+1)] + [n]

        nums.sort()

        return nums == arr
