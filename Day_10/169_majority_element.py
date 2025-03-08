# Time COmplexity O(n)
# Space complexity  = O(N) # hashmap storing each number and count

def majority_element(nums):
    hash_map = {}
    count = 0
    max_value = nums[0]

    for num in nums:
        if num not in hash_map.keys():
            hash_map[num] = 1
        else:
            hash_map[num] += 1
        
        if hash_map[num] > count:
            count = hash_map[num]
            max_value = num
        
    return max_value



if __name__ == "__main__":
    nums = [3,2,3]

    print(majority_element(nums))

    nums = [2,2,1,1,1,2,2]
    print(majority_element(nums))

