class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        N = len(arr)
        
        def dfs(i, seen):
            seen.add(i)

            if arr[i] == 0:
                return True

            good = False

            if i + arr[i] < N and i + arr[i] not in seen:
                good |= dfs(i + arr[i], seen)
            
            if i - arr[i] >= 0 and i - arr[i] not in seen:
                good |= dfs(i - arr[i], seen)

            return good

        return dfs(start, set())
