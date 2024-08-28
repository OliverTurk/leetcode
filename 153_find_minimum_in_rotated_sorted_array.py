class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        current_min = nums[l]

        while l <= r:
            mid = l + (r - l) // 2

            current_min = min(nums[mid], current_min)
            
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid - 1

        return current_min
