class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1 = set()
        set2 = set()

        for n in arr1:            
            while n != 0:
                set1.add(n)
                n //= 10

        for n in arr2:
            while n != 0:
                set2.add(n)
                n //= 10

        intersection = set1 & set2
        
        return len(str(max(intersection))) if intersection else 
