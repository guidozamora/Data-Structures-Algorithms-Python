"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory

Solution
- Loop through the array and store each unique value in a dictionary
- Use a cont to confirm how many times has the value appear
- If any value is already in the dict, remove that value from the array

Time Complexity = O (N)
"""

def removeDuplicates(nums):
    cont = 0
    index = 0
    actual_value = None
    while index < len(nums):
        if nums[index] == actual_value:
            if cont >= 2:
                nums.pop(index)
                index -= 1
            else:
                cont += 1
        else:
            actual_value = nums[index]
            cont = 1
        index += 1
    print(nums)
    return len(nums)

array = [0,0,1,1,1,1,2,3,3]

print(removeDuplicates(array))