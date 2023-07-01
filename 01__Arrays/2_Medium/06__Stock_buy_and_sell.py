# O(N) TC | O(1) TC

def maxProfit(prices):
    currentMinPrice = float('inf')
    maxProfit = 0

    for i in range(len(prices)):
        currentPrice = prices[i]
        if currentPrice > currentMinPrice:
            currentProfit = currentPrice - currentMinPrice
            maxProfit = max(currentProfit, maxProfit)
        elif currentPrice < currentMinPrice:
            currentMinPrice = currentPrice
    
    return maxProfit



# Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# CN: https://www.codingninjas.com/codestudio/problems/893405
# GFG: https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/0