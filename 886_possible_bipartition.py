class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        conns = defaultdict(list)

        for a, b in dislikes:
            conns[a].append(b)
            conns[b].append(a)

        color = {}

        def dfs(a, c):
            if a in color:
                return color[a] == c
            
            color[a] = c

            return all(dfs(b, 1 - c) for b in conns[a])

        return all(dfs(a, 0) for a in range(1, n+1) if a not in color)
