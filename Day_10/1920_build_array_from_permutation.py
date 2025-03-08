def build_array(nums):
    # take 1st element and on that index 
    output = []
    for i in range(len(nums)):
        # iterate over the list, nums. Then, for that number, 
        # go to its corresponding position and put that number 
        # in our result
        result = nums[nums[i]]
        output.append(result)


    return output









if __name__=="__main__":
    nums = [0,2,1,5,3,4]
    print(build_array(nums))