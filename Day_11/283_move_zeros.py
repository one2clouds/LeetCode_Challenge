def move_zeros(nums):

    # using two pointers, left and right to and if non-zero element shifting its location to left index....

    left = 0
    for right in range(len(nums)):
        if nums[right] !=0:
            nums[right], nums[left] = nums[left], nums[right]
            left +=1

    return nums






if __name__ == "__main__":
    nums = [0,1,0,3,12]

    print(move_zeros(nums))

