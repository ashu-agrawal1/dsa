# Question 2

# Python function to find best time to buy and sell a stock
# Running through a loop we are going to keep record of our minimum price and if we got a greater price than our minimum price than we will try to sell and keep record of the profit. At last we will return the max profit
def maxPro(prices):
    min_price = 999999999
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            
    return max_profit
    
    
# Test run

prices = [4, 3,1,8,19,15,7]

maxPro(prices)

Time complexity:O(n), Because single loop is needed.

Space complexity: O(1). 2 variables are used.
