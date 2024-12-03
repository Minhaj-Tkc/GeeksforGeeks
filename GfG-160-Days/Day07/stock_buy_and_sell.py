class Solution:
    def maximumProfit(self, prices) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit


sol = Solution()
output = sol.maximumProfit([100, 180, 260, 310, 40, 535, 695])
print(output)