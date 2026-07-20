class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        neighbours = defaultdict(list)

        for i in range(N):
            neighbours[arr[i]].append(i)

        queue = []
        queue.append(0)
        res = 0
        seen = {0}
        used = set()

        while queue:
            layer = []
            while queue:
                i = queue.pop()

                if i == N-1: return res

                if arr[i] not in used:
                    for j in neighbours[arr[i]]:
                        if j in seen: continue
                        
                        layer.append(j)
                        seen.add(j)

                    used.add(arr[i])

                if i > 0 and i-1 not in seen: 
                    layer.append(i-1)
                    seen.add(i-1)

                if i < N-1 and i+1 not in seen: 
                    layer.append(i+1)
                    seen.add(i+1)

            res += 1
            queue = layer
