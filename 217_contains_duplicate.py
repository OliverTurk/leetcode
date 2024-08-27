class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        digits_seen = set()
        contains_duplicate = False

        for i in nums:
            if i not in digits_seen:
                digits_seen.add(i)
            else:
                contains_duplicate = True

        return contains_duplicate
