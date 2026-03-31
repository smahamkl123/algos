from typing import List

def maxProfit(prices: List[int]) -> int:
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    return total_profit

# prices = [1,2,3,4,5] #
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5,6,5]

total_profit = maxProfit(prices)

print(f"Total profit: {total_profit}")