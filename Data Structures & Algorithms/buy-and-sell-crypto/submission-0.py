class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # There is an order of precedence from left to right
        # Right must be larger than left
        # Find the max difference from a window size
        # Sliding window approach
        # Theres no fixed window size so it can grow larger

        # Start at the left side with window size 1
        # shift the window right if the value is less than the window size
        # Iterate all the way to the end

        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit
                

            
        