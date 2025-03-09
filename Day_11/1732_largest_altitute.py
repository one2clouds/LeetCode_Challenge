# time complexity = O(N)
# space complexity = O(1)

def largest_altitute(nums):
    max_sum = 0
    sum = 0

    for i in range(len(nums)):
        sum += nums[i ]
        max_sum = max(max_sum, sum)

    return max_sum



if __name__ == "__main__":
    nums = [-5,1,5,0,-7]
    print(largest_altitute(nums))

