class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num

        while low<=high:
            mid = low + (high-low)//2
            check = mid**2
            if check < num:
                low = mid+1
            elif check > num:
                high = mid-1
            else:
                return True
        return False