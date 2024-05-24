class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        maxProfit=0
        minPrices=prices[0]
        for price in prices[1:]:
            if price<minPrices:
                minPrices=price
            else:
                maxProfit=max(maxProfit, price-minPrices)
        return maxProfit
