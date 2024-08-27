class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        prefix_product = 1
        post_fix_product = 1

        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            output[i] *= post_fix_product
            post_fix_product *= nums[i]

        return output
