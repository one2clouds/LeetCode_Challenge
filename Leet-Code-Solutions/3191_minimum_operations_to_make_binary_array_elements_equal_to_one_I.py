# Sliding window problem, we take window of 3 and if first element is 0, reverse it to 1. Also, inside the window there are 2nd and 3rd element of window, 
# they will be reversed too, 1 as 0 and 0 as 1. We try to make all numbers 1 and count the minimum operations required. If last 2 numbers will not become 1, then return -1

# Time : O(N) and Space O(1)

def minOperations(nums):
    count = 0
    for i in range(len(nums)-2):
        if nums[i] ==0 and i <len(nums):
            nums[i] = 1 - nums[i]
            nums[i+1] = 1 - nums[i+1]
            nums[i+2] = 1 - nums[i+2]
            count += 1

        if nums[i] == 1:
            continue

    if nums[i+1] == 1 and nums[i+2]==1:
        return count 
    else:
        return -1 


if __name__== "__main__":
    nums = [0,1,1,1,0,0]

    print(minOperations(nums))

    nums = [0,1,1,1]
    print(minOperations(nums))

