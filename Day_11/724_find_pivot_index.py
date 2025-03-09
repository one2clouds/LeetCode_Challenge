# time complexity = O(N) for 'sum' operation and O(N) for loop 
# space complexity = O(1)

def find_pivot_index(nums):
    total = sum(nums) # O(n)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total - nums[i] - left_sum

        if left_sum == right_sum:
            return i 
        left_sum += nums[i]

    return -1



if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    print(find_pivot_index(nums))

