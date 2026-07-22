class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = []
        diff_arr = [0] * n

        for i, j, k, in bookings:
            diff_arr[i-1] += k
            
            if j < n:
                diff_arr[j] -= k

        diff = 0
        for x in diff_arr:
            diff += x
            res.append(diff)
        
        return res
