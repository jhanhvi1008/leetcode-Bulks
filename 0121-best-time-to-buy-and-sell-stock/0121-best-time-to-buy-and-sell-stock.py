class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Lowest price seen so far
        min_price = prices[0]

        # Maximum profit
        max_profit = 0

        # Go through each price
        for price in prices:

            # Update minimum price
            min_price = min(min_price, price)

            # Calculate today's profit
            profit = price - min_price

            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit
        