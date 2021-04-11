"""

"""

def shuffle_array(nums, n):
    i = 0
    j = n
    nums2 = []
    while n <= len(nums) - 1:
        nums2.append(nums[i])
        nums2.append(nums[j])
        n += 1
        i += 1
        j += 1
    return nums2
if __name__ == '__main__':

    nums = [ 1,2,3,4,4,3,2,1]
    n = 4
    print(shuffle_array(nums,n))


