"""
By binary_search O (N log N)

With dictionaries (Hash Tables) O (N)
"""



def binary_search(nums,target,left_index,right_index):
    middle_index = (left_index + right_index) // 2
    
    while right_index >= left_index:
        if nums[middle_index] == target:
            return middle_index

        if nums[middle_index] > target:
            right_index = middle_index - 1

        if nums[middle_index] < target:
            left_index = middle_index + 1

        middle_index = (left_index + right_index) // 2
    return -1

def twoSum(numbers, target):
    for index, num in enumerate(numbers):
        new_target = target - num
        pointer = binary_search(numbers,new_target,index+1,len(numbers)-1)
        if pointer != -1:
            return [index+1, pointer+1]


def twoSumDict (numbers,target):
    past_numbers = {}

    for index in range (0, len(numbers)):
        diferencia = target - numbers[index]
        if diferencia in past_numbers:
            return [past_numbers[diferencia] +1, index + 1]
        else:
            past_numbers[numbers[index]] = index
    return -1




numbers = [2,3,4]
target = 6
print(twoSumDict(numbers,target))




