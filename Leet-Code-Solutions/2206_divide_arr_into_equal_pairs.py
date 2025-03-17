

def divideArray(nums):
    hash_map ={}
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    
    for num, count in hash_map.items():
        if count % 2 !=0:
            return False
    
    return True




if __name__== "__main__":
    nums = [3,2,3,2,2,2]

    print(divideArray(nums))
