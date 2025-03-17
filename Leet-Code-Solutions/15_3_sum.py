
def three_sum(nums):
    nums.sort()
    outputs = []

    for i in range(len(nums)):
        if nums[i] == nums[i-1] and i >0: # same number in previous and this step then skip, also first number is non negative number in sorted list then sum can't be zero 
            continue 
        
        l, r = i+1, len(nums)-1 
        while l<r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum <0:
                l += 1
            elif three_sum >0:
                r-= 1
            else:
                outputs.append([nums[i], nums[l], nums[r]])
                l+=1      # continue to check even after we one solution which gives three sums

                while nums[l] == nums[l-1] and l<r:       # this number is same as last and l<r increase left number
                    l+=1 

    return outputs




if __name__ == "__main__":

    nums = [-1,0,1,2,-1,-4]
    print(three_sum(nums))

