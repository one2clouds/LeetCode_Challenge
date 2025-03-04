
# Solution using dynamic programming
# time_complexity = O(N), space_complexity = O(N)
def maxSubArray(nums):
    dp = [0] * (len(nums)+1) # list of n+1 length, has value 0

    for current in range(len(nums)):
        dp[current] = max(dp[current], dp[current-1]+ dp[current])   # if current_element > prev_element+current_element then, 

    return max(dp[current])  # return value of maximum sum


# Dynamic programming 
# time_complexity = O(N), space_complexity = O(constant) or O(1)
def maxSubArr_2(arr):
    max_sum = arr[0]
    current_sum = 0

    for n in arr:
        if current_sum<0:
            current_sum = 0 # current sum if less than 0 then, no point in adding number before it, so make it 0 to add current number in current_sum after this step
        current_sum += n
        max_sum = max(max_sum, current_sum) # return max of sum between current_sum and max_sum we got before 
    return max_sum

        


if __name__=="__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    print(maxSubArray(nums))




