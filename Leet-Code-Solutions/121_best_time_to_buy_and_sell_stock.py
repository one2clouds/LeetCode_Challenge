def best_time_to_buy_and_sell_stock(prices):
    max_profit = 0
    l,r = 0,1

    while r != len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

        else:
            l=r # if left price is smaller, make right as left to subract with other number after it and calculate max profit
        r = r+1 # right will increase after every iteration

    return max_profit





if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(best_time_to_buy_and_sell_stock(prices))


