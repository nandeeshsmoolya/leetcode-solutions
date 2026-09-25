class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit


# Test cases
solution = Solution()

# Test Case 1: Standard case with profit
prices1 = [7, 1, 5, 3, 6, 4]
print("Test Case 1:", solution.maxProfit(prices1))  # Expected output: 5 (buy at 1, sell at 6)

# Test Case 2: Decreasing prices (no profit possible)
prices2 = [7, 6, 4, 3, 1]
print("Test Case 2:", solution.maxProfit(prices2))  # Expected output: 0

# Test Case 3: Already sorted / continuously increasing
prices3 = [1, 2, 3, 4, 5]
print("Test Case 3:", solution.maxProfit(prices3))  # Expected output: 4 (buy at 1, sell at 5)

# Test Case 4: Flat prices
prices4 = [3, 3, 3, 3]
print("Test Case 4:", solution.maxProfit(prices4))  # Expected output: 0