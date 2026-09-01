class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        cache = [0] * n

        cache[0], cache[1] = 1, 2

        for i in range(2, n):
            cache[i] = cache[i-2] + cache[i-1]
            # print(cache)
        return cache[n-1]