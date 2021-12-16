def apple_stocks(stock_prices):
    # 1. Loop through and find the lowest value so far. Store that index
    # 2. Coninue looping, finding the highest value afterwards
    # 3. How can we prohibit buying and seling on the same minute?

    lowest_price = stock_prices[0]
    highest_profit = float('-inf')

    for price in stock_prices[1:]:
        lowest_price = min(lowest_price, price)
        highest_profit = max(highest_profit, price - lowest_price)

    print(highest_profit)

stock_prices = [10, 8, 5, 1]

apple_stocks(stock_prices)