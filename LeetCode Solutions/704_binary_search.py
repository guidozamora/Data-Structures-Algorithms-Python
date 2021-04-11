import time

def linear_search(num_list,target):
    # Time Complexity O (N)
    for i in range(0,len(num_list)):
        if num_list[i] == target:
            return i
    return -1


def binary_search(nums,target):
    left_index = 0
    right_index = len(nums) -1 
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
        
test_array = [i for i in range (1,10000001)]
target = 10000000


start = time.time()
index = linear_search(test_array,target)
end = time.time()
performance = end - start
print(f'The number {target} is located at index {index}')
print(f'The performance of the linear searchs is {performance}')



start = time.time()
index = binary_search(test_array,target)
end = time.time()
performance = end - start

print(f'The number {target} is located at index {index}')
print(f'The performance of the binary searchs is {performance}')

