from typing import List

def max_profit(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0

    minPrice = prices[0]
    maxProfit = 0

    for i in range(1, len(prices)):
        minPrice = min(prices[i], minPrice)
        maxProfit = max(prices[i] - minPrice, maxProfit)

    return maxProfit

if __name__ == '__main__':
    maxProfit = max_profit([2, 5, 6, 3, 4, 8, 7, 9])
    print(maxProfit)