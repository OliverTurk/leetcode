class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_pairs = [(x,y) for x,y in zip(landStartTime, landDuration)]

        water_pairs = [(x,y) for x,y in zip(waterStartTime, waterDuration)]

        best_land_score = inf

        for x,y in land_pairs:
            if x+y < best_land_score:
                best_land_score = x+y

        best_water_score = inf

        for x,y in water_pairs:
            if x+y < best_water_score:
                best_water_score = x+y
        
        res = inf

        for x, y in water_pairs:
            if x > best_land_score:
                res = min(res, (x - best_land_score) + y + best_land_score)
            else:
                res = min(res, y + best_land_score)

        for x, y in land_pairs:
            if x > best_water_score:
                res = min(res, (x - best_water_score) + y + best_water_score)
            else:
                res = min(res, y + best_water_score)

        return res 
