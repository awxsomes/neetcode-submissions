class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 3:
            return n if n == 1 else n - 1
        low, high = 0, n
        result = 0
        while low <= high:
            
            mid = low + (high-low) // 2
            print(low)
            print(mid)
            print(high)
            coins = mid*(mid+1)/2
            print(coins)
            print()
            if coins > n:
                high = mid-1
            elif coins < n:
                low = mid +1
                result = max(result, mid)

   
        return result