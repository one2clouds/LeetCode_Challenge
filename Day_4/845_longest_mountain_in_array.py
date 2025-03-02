def longest_mountain_in_array(nums):
    result = 0

    for idx in range(1,len(nums)-1): # since there won't be mountain condition at 1st and last index and value before 1st index and after last index doesn't exist

        if nums[idx-1] < nums[idx] and nums[idx] > nums[idx+1]: # check for top of the mountain, i.e. max num
            l = r = idx

            while l>0 and nums[l] > nums[l-1]:
                # for mountain, previous element is smaller than current element, and l>0 for boundary condition check
                l -= 1
            
            while r+1 < len(nums) and nums[r]>nums[r+1]:
                # for mountain, previous element is smaller than current element, and r<len(arr)-1 for boundary condition check
                r += 1 
            
            result = max(result, r-l+1)

    return result





if __name__ == "__main__":
    nums = [2,1,4,7,3,2,5]
    # nums = [2,2,2]
    print(longest_mountain_in_array(nums))




