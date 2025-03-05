def subsets(nums):
    subset = []
    output = []



    # add all elements of the list recursively at first, then append it there, then go out of each recursive loop and pop each element to get empty subset, [] at last.
    def backtracking(i):
        if i >= len(nums):
            output.append(subset[:])
            return

        
        # whether or not to include ith number in our subset list 
        # include ith number recursively apply backtracking function to i+1 term
        subset.append(nums[i])
        backtracking(i+1)

        # don't include ith number and recursively apply backtracking function to i+1 term 
        subset.pop()
        backtracking(i+1)

    backtracking(0)

    return output




if __name__=="__main__":
    nums = [1,2,3]
    print(subsets(nums))

