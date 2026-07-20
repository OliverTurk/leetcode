class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = [0] * 51
        seen_b = [0] * 51

        N = len(A)

        count = 0

        res = [0] * N 
        for i in range(N):
            if not seen_a[A[i]] and seen_b[A[i]]:
                count += 1
            
            seen_a[A[i]] = 1

            if not seen_b[B[i]] and seen_a[B[i]]:
                count += 1
            
            seen_b[B[i]] = 1

            res[i] = count

        return res
