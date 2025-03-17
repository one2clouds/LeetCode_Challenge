

def min_abs_difference(nums):
    # sort the numbers of array 
    nums.sort()
    min_diff = float('inf')
    
    # check for the minimum difference 
    for i in range(1, len(nums)):
        min_diff = min(min_diff, nums[i] - nums[i-1])

    # keep the number in list having minimum difference 
    result = []
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] == min_diff:
            result.append([nums[i-1], nums[i]])

    return result



if __name__ == "__main__":

    nums = [1, 2, 3, 4, -1, -2, 8, 10, 15]

    print(min_abs_difference(nums))
