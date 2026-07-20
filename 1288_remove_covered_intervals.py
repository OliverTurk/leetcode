class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        
        intervals.sort(key=lambda x: (x[1], -x[0]))

        res = N
        min_start = inf
        for i in range(N-1, -1, -1):
            a = intervals[i][0]

            if min_start <= a:
                res -= 1

            min_start = min(min_start, a)
            
        return res
