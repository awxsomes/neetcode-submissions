import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        def eattime(piles, rate):
            summation = 0
            for i in piles:
                summation += math.ceil(i/rate)
            return summation
        fin = high
        while low <= high:
            mid = low + (high-low)//2
            print(mid)
            
            ti = eattime(piles,mid)
            print(ti)
            print()
            if ti <= h:
                fin = mid
                high = mid-1
            else:
                low = mid+1
        return fin