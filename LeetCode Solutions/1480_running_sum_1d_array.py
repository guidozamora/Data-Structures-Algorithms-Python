"""
Solution steps:
- Create a sum variable and set it to zero
- Loop thru the array
- Add the value of each element to a the sum variable
- Add each sum to a new list
"""

def runningSum (nums):
    sum = 0
    sum_nums = []
    for number in nums:
        sum += number
        sum_nums.append(sum)
    return sum_nums

print(runningSum([1,1,1,1,1]))
