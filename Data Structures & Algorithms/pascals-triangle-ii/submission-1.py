class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (i + 1) for i in range(rowIndex+1)]

        for i in range(2, rowIndex+1):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[-1]