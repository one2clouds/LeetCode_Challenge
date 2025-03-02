def contains_duplicates(nums, k):
    L = 0 
    window = set()

    for R in range(len(nums)):
        if R-L > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True 
        window.add(nums[R])
    
    return False 
    




if __name__ == "__main__":

    nums = [1,2,3,1]
    k = 3

    print(contains_duplicates(nums, k))

