
def remove_element(nums, val):
    ''' Basically we iterate over the list, 
    and only add element in location from k=0 
    if each element of nums != val '''
    
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        else:
            continue
    return k 
        










if __name__ == "__main__":
    nums = [1,4,2,4,4,2,1,2]
    k = remove_element(nums, 4)
    print(k)

