def missing_number(nums):
    '''
    first sort numbers in order. Then, if index is not equal to number, the number is missing. 
    Also, exception arise when in case : [1,2,3] where actually list is of size 4 and number 4 is missing.
    '''

    nums.sort()
    for i,num in enumerate(nums):
        if i != num:
            return i # or num-1

        if i == len(nums)-1:
            return i+1 #or num +1 
        
def missing_number_best(nums):
    '''
    using inbuilt sum function and range to get missing number can help
    '''
    return sum(range(len(nums)+1)) - sum(nums)



if __name__ == "__main__":
    nums = [1,4, 0, 2,3, 6] # print missing number from unsorted list in range(1,6)
    print(missing_number(nums))
    print(missing_number_best(nums))