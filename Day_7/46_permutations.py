
# go inside recursive loop until len(nums) == 0, then at last (l) layer of recursion perms = [[]] and nums = [], 
    # break out of that, then p_copy = perms = [[]], nums=[3] in l-1 layer, after for loops perms=p_copy = [[3]] =  outputs=[[3]], in l-2 layer, perms = [[3]], nums=(2,3), 
    # after for loop perms=p_copy = [[2,3], [3,2]] as len(p)+1==2 = len(nums) so loop executed 2 time to get those. Then in l-3 or 1st iteration, perms = [[2,3],[3,2]], nums = (1,2,3),
    #  len(p)+1=3, then p = [2,3] in perms, add 1 in start, middle and end, p = [3, 2] in perms, add 1 in start, middle and end.

# Time complexity
    # for n numbers we need n permutations, so n! 
    # inserting 1 element in n permutations = n 
    # inserting n element in n permutations = n^2. 
    # So overall time complexity = O(n!*n^2)

# Space Complexity 
# maximum recursion depth = O(n)
# max number of permutations = O(n!)
# so overall space complexity = O(n * n!)


def permutations(nums):

    if len(nums) == 0:
        return [[]]   # base case 
    
    perms = permutations(nums[1:])   

    outputs = []
    
    for p in perms:
        for i in range(len(p)+1):
            p_copy = p[:] # shallow copy 
            p_copy.insert(i, nums[0])
            outputs.append(p_copy)

    return outputs



if __name__=="__main__":
    nums = [1,2,3]
    print(permutations(nums))

