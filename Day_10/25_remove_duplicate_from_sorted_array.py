

def remove_duplicates(nums):
    left = 1

    # set left to 1, increase right from by 1 to len(nums)      
    for right in range(1, len(nums)):
        # current item, not equal to previous....
        if nums[right] != nums[right-1]:
            # at location of left pointer value put item from right pointer
            nums[left] = nums[right]
            left += 1
    return left
        

if __name__ == "__main__":
    nums = [1,1,2]
    print(nums[:remove_duplicates(nums)])