class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)

        colours = {}

        def dfs(a, c):
            if a in colours:
                return colours[a] == c

            colours[a] = c

            return all(dfs(b, 1-c) for b in graph[a])

        return all(dfs(a, 0) for a in range(N) if a not in colours) 
