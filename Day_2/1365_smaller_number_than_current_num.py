def smallerNumberthancurrent(nums):
    '''
    Logic : basically after sorting numbers, its location will correspondingly 
    give how many numbers are smaller than it. A dictionary is used to store 
    number and its location to be retrieved afterwards. 
    '''

    temp = sorted(nums)

    hash_map = {}

    for i,n in enumerate(temp):
        if n not in hash_map:
            hash_map[n] = i

    output = []

    for i in nums:
        output.append(hash_map[i])

    return output

if __name__ == "__main__":
    nums = [1,4,3,6] 
    print(smallerNumberthancurrent(nums))
