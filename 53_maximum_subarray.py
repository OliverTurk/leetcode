class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        
        current_sum = 0

        for i in range(len(nums)):

            current_sum += nums[i]
            
            sums.append(current_sum)
            
            if current_sum < 0:
                current_sum = 0
        
        if not sums:
            return -1

        return max(sums)
