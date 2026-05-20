class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if (price < min_price):
                min_price = price
            current_profit = price - min_price
            if max_profit < current_profit:
                max_profit = current_profit
        return max_profit
        # go through prices
        # update current minimum every price encountered 
        # if current profit is higher than max profit, update max profit
        