
def countBits(num):
    dp = [0] * (n+1)
    offset = 1


    for i in range(num+1):
        if offset*2 == i:
            offset =i 
        dp[i] = 1+ dp[i-offset]
        
    return dp 


if __name__ == "__main__":
    n = 10
    print(countBits(n))





