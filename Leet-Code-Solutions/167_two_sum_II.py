def two_sum_II(nums, target):
    '''
    Logic : for sorted input, we know it is increasing from left to right. 
    If sum is lesser we need to increase sum to meet target so l shifts 
    right. If sum is more than target decrease sum by shifting r left. 
    '''
    l, r = 0, len(nums)-1
        
    while l<r:
        sum_nums = nums[l] + nums[r]
        if sum_nums < target:
            l += 1
        elif sum_nums > target:
            r -= 1
        else:
            return [l,r]

if __name__ == "__main__":
    nums = [1,4,3,6] 
    target = 7
    print(two_sum_II(nums, target))
