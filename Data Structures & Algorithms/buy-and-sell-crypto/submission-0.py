class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            goal: given prices (prices[i] = price of neetcoin on ith day) 
            [10,1,5,6,7,1]            
            choose a day to buy 1 neetcoin and another day to sell
            return max profit
        '''

        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return maxProfit
        
