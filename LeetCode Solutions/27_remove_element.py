'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Time Complexity: O(N) where N is the number of elements in nums
Space Complexity: O(1)

'''

def remove_element(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = 101
    nums.sort()
    new_length = len(nums) - nums.count(101)
    return new_length

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 2

    print(remove_element(nums,val))