"""
TC = O(n)
"""

def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1
    for num in nums2:
        nums1[m] = num
        m += 1
    nums1.sort()
    return nums1

numeros1 = [1,2,3,0,0,0]
m = 3
numeros2 = [2,5,6]
n = 3

numeros_final = merge(numeros1,m,numeros2,n)

print(numeros_final)