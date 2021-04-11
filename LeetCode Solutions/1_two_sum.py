"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Solution
- Loop through the array
- Sum the array element on i + the array element on i +1
- if the sum = to target return a list containing i and i+1

Time complexity is O (N square) for twoSum and O (N) for twoSumDic
 """

def twoSum (nums, target):
    for i in range (0,len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSumDic (nums, target):
    dict_nums = {}
    for i in range (0,len(nums)):
        n = target - nums[i]
        if n not in dict_nums:
            dict_nums[nums[i]] = i
        else:
            return [dict_nums[n],i]


print (twoSumDic([2,5,5,11],10))