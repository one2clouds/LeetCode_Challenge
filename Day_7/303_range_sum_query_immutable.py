
#time complexity : O(N) iterating from left:right+1
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])
    

# Better Solution
# time complexity : O(N), better approach because we need to O(N) computation only once
class NumArray_2(object):
    def __init__(self, nums):
        self.acc_nums = [0]

        for i in nums:
            self.add_nums = sum(self.acc_nums[-1] + i)

    def sumRange(self, left, right):
        return self.acc_nums[right+1] - self.acc_nums[left]

"""
# Input 

["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

# Output 
[null,1,-1,-3]

"""

