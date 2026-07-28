class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q = deque()

        q.append((0, x))

        seen = set()
        best = inf

        while True:
            l, x = q.popleft()

            if l > best:
                break

            if x in seen: 
                continue
            
            seen.add(x)

            if x == y:
                best = min(best, l)

            q.append((l + 1, x + 1))

            if x % 11 == 0:
                q.append((l + 1, x // 11))
            if x % 5 == 0:
                q.append((l + 1, x // 5))
            if x > 1:
                q.append((l + 1, x - 1))

        return best
