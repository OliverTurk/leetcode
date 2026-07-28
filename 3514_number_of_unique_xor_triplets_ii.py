class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs = set()
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                pairs.add(nums[i] ^ nums[j])

        triplets = set()

        for x in nums:
            for p in pairs:
                triplets.add(x ^ p)

        return len(triplets)

