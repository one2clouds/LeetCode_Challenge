# dynamic programming is computer programming technique 
# where algorithm problem is first broken down into 
# subproblems the results are saved and then reused 
# to find a solution effectively. 


def coin_change(coins, amount):

    dp = [amount + 1] (amount+1) # [amount+1] makes list of value (amount+1)
    dp[0] = 0 # if amount=0 then min con required is 0


    for a in range(1, amount+1):
        for c in coins:
            if a-c >=0: # if a-c is non negative number 
                dp[a] = min(dp[a], 1+dp[a-c])    # dp[7] = min(dp[7], 1+ dp[7-6]) then we put dp[1] in above afterwards........

    return dp[amount] if dp[amount]!=amount + 1 else -1      # return dp[amount] if it is other than previously initialized value else -1


if __name__ == "__main__":
    nums = [1,2,5]
    amount = 11
    print(coin_change(nums, amount))




