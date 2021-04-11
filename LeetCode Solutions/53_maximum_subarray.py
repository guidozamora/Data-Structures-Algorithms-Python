'''
Solution:
- Iterate thru the array
- when a positive number is found, start suming it until

'''

def max_subarray(nums):
    # sum_current = 0
    # max_sum = -99999999999999

    # for num in nums:
    #     sum_current = sum_current + num
    #     max_sum = max(sum_current,max_sum)
    #     if sum_current < 0:
    #         sum_current = 0
    # return max_sum

    subarray = []
    subarray.append(nums[0])
    

    for i in range (1,len(nums)):
        subarray.append(max(nums[i], subarray[i-1] + nums[i]))
    return max(subarray)




if __name__ == "__main__":
    nums = [0]

    print(max_subarray(nums))
    