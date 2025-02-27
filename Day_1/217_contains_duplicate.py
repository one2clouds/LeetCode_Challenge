def contains_duplicate(nums):
    '''
    nums is a list, for checking duplicates we can use inbuild sets, 
    which doesn't store duplicates. Checking their length gives us solution.
    '''


    if len(set(nums)) == len(nums):
        return True 
    else:
        return False


if __name__ == "__main__":
    nums = [1,2,3,3,3]
    print(contains_duplicate(nums))