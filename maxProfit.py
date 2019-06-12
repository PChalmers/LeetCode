class Solution:

    def maxProfit2(self, prices, fee):
        dp = [0] * len(prices)
        for j in range(len(dp)):
            dp[j] = dp[j -1]
            for i in range(j):
                dp[j] = max(dp[j], +prices[j] - prices[i] - fee + (dp[i - 1] if i - 1 >=0 else 0))
                print(j, i, dp)
        return dp[-1]


s = Solution()
print(s.maxProfit2([1, 3, 2, 8, 4, 9], 2))