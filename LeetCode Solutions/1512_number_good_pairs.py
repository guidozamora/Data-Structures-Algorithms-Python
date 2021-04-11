'''
Time Complexity: O(N squared)
Space Complexity: O(1)

'''


def number_good_pairs(nums):
    pairs = 0
    for i,n in enumerate(nums[:-1]):
        j = i+1
        while j < len(nums):
            if n == nums[j]:
                    pairs += 1
            j += 1
    return pairs


if __name__ == '__main__':
    nums = [1,2,3]

    print(number_good_pairs(nums))