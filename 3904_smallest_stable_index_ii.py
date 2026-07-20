class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max = []
        cur = 0
        for n in nums:
            cur = max(cur, n)
            prefix_max.append(cur)

        suffix_min = []
        cur = inf
        for n in nums[::-1]:
            cur = min(cur, n)
            suffix_min.append(cur)

        suffix_min = suffix_min[::-1]

        N = len(nums)

        for i in range(N):
            score = prefix_max[i] - suffix_min[i]

            if score <= k:
                return i

        return -1

