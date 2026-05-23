#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums,target):
    num_map={}
    for i, num in enumerate(nums):
        complement=target-num
        if complement in num_map:
            return [num_map[complement],i] 
        num_map[num]=i
    return []

test_num=[2,7,11,15]
test_target=9

result=two_sum(test_num,test_target)
print("The indices are :" ,result)