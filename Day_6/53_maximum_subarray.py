
# Solution using dynamic programming
# time_complexity = O(N), space_complexity = O(N)
def maxSubArray(nums):
    dp = [0] * (len(nums)+1) # list of n+1 length, has value 0

    for current in range(len(nums)):
        dp[current] = max(dp[current], dp[current-1]+ dp[current])   # if current_element > prev_element+current_element then, 

    return max(dp[current])  # return value of maximum sum


def 


if __name__=="__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))




