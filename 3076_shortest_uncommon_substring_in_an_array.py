class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        N = len(arr)

        res = []

        def good(s, skip):
            for i in range(N):
                if i == skip:
                    continue
                
                if s in arr[i]:
                    return False
            
            return True


        for i in range(N):
            s = arr[i]
            n = len(s)
            flag = False
            smallest = s

            for j in range(n):
                for k in range(j+1, n+1):
                    x = s[j:k]
                    if good(x, i):
                        print(x)
                        flag = True

                        if len(x) < len(smallest):
                            smallest = x
                        elif len(x) == len(smallest):
                            smallest = min(smallest, x)
                    
            if flag:
                res.append(smallest)
            else:
                res.append("")

        return res
