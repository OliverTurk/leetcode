class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots = []
        less_than = []
        greater_than = []

        for n in nums:
            if n < pivot:
                less_than.append(n)
            elif n > pivot:
                greater_than.append(n)
            else:
                pivots.append(n)

        return less_than + pivots + greater_tha
