class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        freq = defaultdict(int)

        for n in nums: freq[n] += 1


        unique_nums = sorted(freq)
        present = set(unique_nums)

        max_val = max(unique_nums)

        best = {x : x for x in unique_nums}

        for d in unique_nums:
            for m in range(d, max_val+1, d):
                if m in present:
                    best[m] = min(best[m], d)

        return sum(best[d] * freq[d] for d in unique_nums)
