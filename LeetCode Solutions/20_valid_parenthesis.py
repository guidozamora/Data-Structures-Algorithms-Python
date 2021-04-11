"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid

Solution
- Create a dictionary with the each parenthesis and -1 for all values
- Loop thru the string and open and close parenthesis with boolean variables

Time Complexity = O(n) where n is the number of elements in the string
Space Complexity = 0(1)


Test cases:

() -> True
()[]{} -> True
(] -> False
([)] -> False
{[]} -> True

"""

from collections import deque

def is_valid(s):
    stack = deque()
    opening = ['(','[','{']
    closing = [')',']','}']

    # Validates if the array is empty
    if len(s) == 0: return True

    # Validates if the array has an odd number of characters in which case the string can not be a valid parenthesis
    if len(s) % 2 != 0: return False

    # Loop through each element of the string
    for char in s:
        if char in opening:
            stack.append(char)
        if char in closing:
            if len(stack) == 0: return False
            else:
                last_character = stack.pop()
                closing_index = closing.index(char)
                openings_index = opening.index(last_character)
                if closing_index != openings_index:
                    return False
    return len(stack) == 0

if __name__ == "__main__":
    
    string = '))'

    print(is_valid(string))