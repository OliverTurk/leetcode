class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = 0
        r = len(arr) - 1

        while l < r:
            gap = r - l
            if arr[l+1] > arr[l]:
                l += 1
            if arr[r-1] > arr[r]:
                r -= 1

            if r - l == gap:
                return False

        if r == 0 or l == len(arr) - 1:
            return False
            
        return True
