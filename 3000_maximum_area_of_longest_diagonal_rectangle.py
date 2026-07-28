class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_area = best_diagonal = 0

        for l, w in dimensions:
            diag = sqrt((l * l) + (w * w))

            if diag > best_diagonal:
                best_diagonal = diag
                best_area = l * w
            elif diag == best_diagonal:
                best_area = max(best_area, l * w)

        return best_area
