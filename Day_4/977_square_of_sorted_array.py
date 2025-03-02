# Trival Solution 
# Time complexity => (N) + (NlogN) = N logN
def square_of_sorted_array(nums):
    sq_nums = [num**2 for num in nums]
    sq_nums.sort()
    return sq_nums





if __name__ == "__main__":
    # nums = [-4,-1,0,3,10]

    nums = [-4,-3,-2,-1]
    print(square_of_sorted_array(nums))

