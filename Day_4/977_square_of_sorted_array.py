# Trival Solution 
# Time complexity => (N) + (NlogN) = N logN
def square_of_sorted_array(nums):
    sq_nums = [num**2 for num in nums]
    sq_nums.sort()
    return sq_nums

# Good Solution 
# Time complexity => O(N)
# merge function = O(N)
# to get pos_index = O(N)
# to create A and B = O(N)
def square_of_sorted_array_2(nums):
    # -----------------------------------------------
    def merge(A,B):
        a=b=0
        ret = []

        while a<len(A) and b<len(B): # both a,b are less than len of  A,B respectively
            if A[a] < B[b]:
                ret.append(A[a])
                a+=1
            else:
                ret.append(B[b])
                b+=1
        
        if a<len(A):
            ret.extend(A[a:]) # We have appended all values of B in list and some A. Now, some values of A remain in list, we append them, one by one as it is already sorted.
        
        else:
            ret.extend(B[b:]) # We have appended all values of A in list and some B. Now, some values of B remain in list, we append them, one by one as it is already sorted.


        return [n**2 for n in ret]
    # -------------------------------------------------

    if not nums:
        return nums  # for not numbers 

    if nums[0]>0:
        return [num**2 for num in nums] # for positive numbers only, as list is sorted, we square.

    pos_index = len(nums) # we assume no positive numbers exist in list, and if it exists, it exists from i
    for i,n in enumerate(nums):
        if n>=0:
            pos_index = i
            break
    
    A = nums[pos_index:]
    B = [-1*num for num in reversed(nums[:pos_index])]
    
    return merge(A,B)





if __name__ == "__main__":
    # nums = [-4,-1,0,3,10]

    nums = [-4,-3,-2,-1]
    print(square_of_sorted_array(nums))

