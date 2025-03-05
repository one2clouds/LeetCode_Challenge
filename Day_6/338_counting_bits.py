
# time complexity = O(N)
def countBits(num):
    dp = [0] * (n+1)
    offset = 1

    # for example if we have i=8, then previously our offset was at 4, i.e 
    # no. of bits become 1 again as 4 = 100, current as 4*2 = 8, so offset 
    # becomes 8 and number of bits for  becomes 1 again and increases until 
    # next offset i.e 16
    
    for i in range(num+1):
        if offset*2 == i:
            offset =i 
        dp[i] = 1+ dp[i-offset] # 
        
    return dp 


if __name__ == "__main__":
    n = 10
    print(countBits(n))





