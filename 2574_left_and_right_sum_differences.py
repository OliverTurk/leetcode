class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_sum = [0]
        
        cur_sum = 0
        for i in range(N-1):
            cur_sum += nums[i]
            left_sum.append(cur_sum)

        right_sum = [0]
        
        cur_sum = 0
        for i in range(N-1, 0, -1):
            cur_sum += nums[i]
            right_sum.append(cur_sum)

        right_sum.reverse()

        res = []
        for i in range(N):
            res.append(abs(left_sum[i] - right_sum[i]))

        return res
