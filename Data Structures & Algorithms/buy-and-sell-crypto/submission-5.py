import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return None
        max_profit = 0
        # find max within range after prices[i]
        # if max not > 0 or prevmax, ignore this index
        def findProfit(index, market):
            market_watch = market[index:]
            current_price = market_watch[0]
            max_future_price = max(market_watch)
            if ((max_future_price - current_price) > 0):
                return max_future_price - current_price
            return 0
        for i in range(len(prices)):
            max_profit = max(findProfit(i, prices), max_profit)
        return max_profit
# line 10
# i = 1
# max = 0
# input prices = [10,1,5,6,7,1]
# market_watch = [1,5,6,7,1]
# output = 