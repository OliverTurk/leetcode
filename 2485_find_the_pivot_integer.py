class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0]

        cur = 0
        for x in range(1, n+1):
            cur += x
            prefix.append(cur)

        for i in range(1,n+1):
            if prefix[i] == prefix[-1] - prefix[i-1]:
                return i

        return -1
