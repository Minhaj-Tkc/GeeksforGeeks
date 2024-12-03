class Solution:
    def maximumProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0  # No profit possible with less than 2 prices

        min_price = float('inf')  # Initialize to infinity
        max_profit = 0

        for price in prices:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)
            # Calculate the profit for the current price and update max profit
            max_profit = max(max_profit, price - min_price)

        return max_profit
    

sol = Solution()
output = sol.maximumProfit([3, 6])
print(output)