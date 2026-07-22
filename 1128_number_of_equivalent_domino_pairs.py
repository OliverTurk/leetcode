class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0

        freq = defaultdict(int)

        for a, b in dominoes:
            res += freq[(a,b)]
            if a != b:
                res += freq[(b,a)]
            freq[(a, b)] += 1
        
        return res           

