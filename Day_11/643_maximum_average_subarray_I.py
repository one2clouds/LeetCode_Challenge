def find_max_average(nums, k):

    # taking first k numbers and summing it and initializing it as max_sum
    current_sum = sum(nums[:k])
    max_average = float(current_sum) / k

    left = 0

    # from k to last item, remove first element accessed from left, add current element, then find max, and increase left pointer accordingly from 0 and right pointer from k
    for right in range(k, len(nums)):
        current_sum -= nums[left]
        current_sum += nums[right]

        max_average = max(max_average, float(current_sum)/k)
        left += 1

    return max_average


if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4

    print(find_max_average(nums, k))




