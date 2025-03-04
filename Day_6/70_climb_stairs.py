def climb_stairs(n):
    dp = [0] * (n+1)  # store values from 0 to n

    if n == 1: # for edge cases
        return 1
    if n == 2: # for edge cases, 
        return 2
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] # we can only take one or two steps

    return dp[n]


if __name__ == "__main__":
    n = 10
    print(climb_stairs(n))




