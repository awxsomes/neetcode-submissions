class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, hi = 1, max(piles)
        res = 0
        while l <= hi:
            mid = l + (hi-l) // 2
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i/mid)

            if totalTime <= h:
                res = mid
                hi = mid - 1
            elif totalTime > h:
                l = mid + 1
                
        return res
