class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        greatestCandies = []
        
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                greatestCandies.append(True)
            else:
                greatestCandies.append(False)
        
        return greatestCandies