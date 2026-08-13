class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        
        mid = low + (high-low)//2
        

        while low<=high:
            mid = low + (high-low)//2
            check = mid**2
            if check < x:
                low = mid+1
            elif check > x:
                high = mid-1
            else:
                return mid
        return high