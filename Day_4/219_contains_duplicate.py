def contains_duplicates(nums, k):
    seen = set()

    for i,num in enumerate(nums):
        if num in seen:   # if number in set then return true 
            return True 
        seen.add(num) # add number 

        if len(seen) > k : # if length of our set is greater than k then remove i-k i.e if i=5& k =3 , remove 5-3=2nd item from set 
            seen.remove(nums[i-k])
    return False 
    




if __name__ == "__main__":

    nums = [1,2,3,1]
    k = 3

    print(contains_duplicates(nums, k))

