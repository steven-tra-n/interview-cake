def apple_stocks(stock_prices):
    # 1. Initialize the first buy and sell as the highest profit so far
    # 2. Since we can't buy and sell on the same minute, start the loop after the first index
    # 3. Update the min and max values in the loop

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit needs at least 2 prices')

    # 1.
    lowest_price = stock_prices[0]
    highest_profit = stock_prices[1] - stock_prices[0]

    # 2.
    for price in stock_prices[1:]:
        # 3.
        potential_profit = price - lowest_price
        highest_profit = max(highest_profit, potential_profit)

        lowest_price = min(lowest_price, price)

    print(highest_profit)

stock_prices = [10, 7, 5, 11, 4]


apple_stocks(stock_prices)