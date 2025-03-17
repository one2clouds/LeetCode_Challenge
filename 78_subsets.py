"""
Time complexity = O(n. 2^n)     # for list of size n, each element has choice of including it or excluding. Resulting in 2^n subset. & for each node it requires O(n) time. So O(n.2^n)
Space complexity = O(n. 2^n)    # 2^n subsets and each subset can be of size at most n
"""

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

