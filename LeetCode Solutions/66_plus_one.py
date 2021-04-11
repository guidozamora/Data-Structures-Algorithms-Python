'''
Solution
- loop the array backwards
- if array[i] == 9, set it to zero
- when it is not 9, array[i] += 1
- if array[0] == 9, add a 1 in the first position of the array

Time Complexity = O(N) where N is the number of elements in the array
Space Complexity = O(1)
'''

def plus_one(digits):

    for index,value in reversed(list(enumerate(digits))):
        if value != 9:
            digits[index] = value + 1
            break
        else:
            digits[index] = 0
            if index == 0:
                digits.insert(0,1)
    return digits



if __name__ == "__main__":
    digits = [9,9]

    print(plus_one(digits))