class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftMin = float('inf')
        result = float('-inf')
        for i in range(len(prices)):
            curr = prices[i]
            result = max(result, curr - leftMin)
            leftMin = min(curr, leftMin)
        if result < 0:
            return 0
        return result
