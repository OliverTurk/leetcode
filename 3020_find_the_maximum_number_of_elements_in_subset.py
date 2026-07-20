class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        best = 0
        cur = 0

        for n in sorted(list(freq.keys())):
            x = n
            while x in freq:
                if freq[x] == 1:
                    cur += 1
                    break

                cur += 2

                freq[x] -= 2

                if freq[x] <= 0:
                    del freq[x]

                x *= x

                if x not in freq:
                    cur -= 1
                    break 

            best = max(best, cur)

            cur = 0

        return best 
