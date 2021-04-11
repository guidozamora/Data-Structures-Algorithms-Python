"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Solution
- Loop through the array and store each unique value in a dictionary
- If any value is already in the dict, remove that value from the array

Time Complexity = O (N)
"""

# def removeDuplicates(nums):
#     existing_numbers = {}
#     index = 0
#     while index < len(nums):
#         if nums[index] in existing_numbers:
#             nums.pop(index)
#             index -= 1
#         else:
#             existing_numbers[nums[index]] = index
#         index += 1
#     return len(nums)

def removeDuplicates(nums):
    index = 0
    actual_value = None
    while index < len(nums):
        if nums[index] == actual_value:
            nums.pop(index)
            index -= 1
        else:
            actual_value = nums[index]
        index += 1
    print(nums)
    return len(nums)

array = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(array))