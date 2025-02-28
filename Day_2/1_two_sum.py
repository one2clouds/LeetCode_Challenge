def two_sum(nums, target):
    '''
    Logic : put 1st element in hashmap, and for 2nd element if target-2nd element 
    will be equal to 1st element then location of 1st and 2nd element is given. 
    But there might be multiple elements which can give sum to target so, we go 
    toward end of list ----> i==len(nums)-1  <---- which gives lists of lists whose 
    sum is equal to target 
    '''

    hash_map = {}
    output = []

    for i,n in enumerate(nums):
        difference = target-n
        if difference in hash_map:
            output.append([hash_map[difference], i])
        else:
            hash_map[n] = i
        if i == len(nums)-1:
            if len(output) == 1:
                return output[0]
            else:
                return output

if __name__ == "__main__":
    nums = [1,4,3,6] 
    target = 7
    print(two_sum(nums, target))
