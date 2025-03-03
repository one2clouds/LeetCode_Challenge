
def min_subarray_sum(nums, target):
    l = 0
    total = 0
    min_size_length = float('inf')

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            min_size_length = min(min_size_length, r-l+1)
            total -= nums[l]
            l += 1

    if min_size_length == float('inf'):
        return 0
    else:
        return min_size_length
    

if __name__ == "__main__":
    nums = [2,1,1,2,4,3]
    target = 7

    print(min_subarray_sum(nums, target))
