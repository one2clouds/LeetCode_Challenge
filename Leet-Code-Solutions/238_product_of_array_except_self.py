
def productExceptSelf(nums):
    res = [1] * len(nums)

    # put prefix=1, then for each index, multiply all the elements before that index
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # put postfix =1, then iterate from last, (postfix = multiply all elements after that 
    # element) then multiply that with prefix element of that index to get multiplication 
    # from allprefix and postfix of that element

    # also while after getting result for each element from last, update the postfix element 
    # like we updated the prefix element : postfix *= nums[i] which multiplies element after the index



    # from (length nums) -1, up to -1, and decrement by -1 
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))

    nums = [-1,1,0,-3,3]
    print(productExceptSelf(nums))


