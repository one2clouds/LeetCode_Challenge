
# Triviaal solution 
# Time Complexity: O(N) 
# Space Complexity: O(N) - We store counts for each unique number in the hashmap
def single_number(nums):
    hash_map = {}
    for num in nums:
        if num not in hash_map.keys():
            hash_map[num] = 1
        else:
            hash_map[num] += 1
    
    for num, counts in hash_map.items():
        if counts == 1:
            return num
        
# Good solution using bitmap 
def single_number_2(nums):
    res = 0 
    for n in nums:
        res = n ^ res  # xor for binary of res....
        # print(res)
    return res 
    

if __name__ == "__main__":
    nums = [2,1,4,2,4, 3, 3]
    # print(single_number(nums))

    print(single_number_2(nums))
