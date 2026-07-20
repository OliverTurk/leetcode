class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        N = len(nums)

        l = 0
        r = N - 1

        asc = nums[l]
        des = nums[r]

        while l != r:
            if nums[l] < nums[l+1]:
                asc += nums[l+1]
                l += 1
            else:
                des += nums[r-1]
                r -= 1
        
        return 0 if asc > des else 1 if des > asc else -1
