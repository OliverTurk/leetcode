class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []

        for x in nums:
            stack.append(x)

            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.append(stack.pop() * 2)

        return stack
