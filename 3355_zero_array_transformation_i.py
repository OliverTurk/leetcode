class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] -= 1
            diff[r+1] += 1

        cur_diff = 0
        for i in range(n):
            cur_diff += diff[i]
            if max(0, nums[i] + cur_diff) != 0:
                return False

        return True
        
