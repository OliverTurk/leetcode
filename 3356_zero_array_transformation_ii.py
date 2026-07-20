class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)

        l = 0
        r = len(queries)

        def good(k):
            diff = [0] * (N + 1)

            for l, r, val in queries[:k]:
                diff[l] += val
                diff[r+1] -= val
            
            cur_diff = 0
            for i in range(N):
                cur_diff += diff[i]

                if cur_diff < nums[i]:
                    return False

            return True 


        while l < r:
            m = (l + r) // 2

            if good(m):
                r = m
            else:
                l = m + 1

        return l if good(l) else -1
