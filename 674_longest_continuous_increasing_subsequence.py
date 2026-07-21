class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        cur = 1

        for a, b in zip(nums, nums[1:]):
            if a < b:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1

        res = max(res, cur)

        return res
