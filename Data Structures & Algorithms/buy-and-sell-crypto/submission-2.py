class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        if len(prices) == 1:
            return 0
        else:
            maxProfit = 0
            while right < len(prices):
                if left < len(prices) and prices[right] < prices[left]:
                    left += 1
                else: 
                    maxProfit = max(prices[right] - prices[left], maxProfit)
                    right += 1

            return maxProfit