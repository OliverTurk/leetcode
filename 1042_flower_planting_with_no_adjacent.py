class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        connections = defaultdict(list)

        for x, y in paths:
            connections[x].append(y)
            connections[y].append(x)

        colours = [1, 2, 3, 4]

        res = [0] * n

        def dfs(a):
            seen = []

            for b in connections[a]:
                if res[b-1]:
                    seen.append(res[b-1])

            for c in colours:
                if c not in seen:
                    res[a-1] = c
                    break
            
            for b in connections[a]:
                if not res[b-1]:
                    dfs(b)

        for i in range(1, n+1):
            if not res[i-1]:
                dfs(i)

        return res

