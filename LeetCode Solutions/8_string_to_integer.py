"""
Implement a function that receive a string and returns an integer

Solution:
- Loop thru the string backgards
- Convert each element to itsnumber value multiplied by its correspondant base
- If the first element of the string is a - multiply the final number by -1

Time Complexity: O(n) n = number of characters in your input string
Space Complexity: O(1) Only 4 variables and max value is INT_MAX for result

"""
def myAtoi (s):
    
    INT_MAX = 2 ** 31 -1
    INT_MIN = -2 ** 31

    i = 0
    sign = 1
    result = 0
    valid_digits = set('0123456789')

    # return 0 if string is empty
    if len(s) == 0: return 0

    #Remove the whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1

    #Detect sign
    if i < len(s) and s[i] == '-':
        i += 1
        sign = -1
    elif i < len(s) and s[i] == '+':
        i += 1

    # check number
    while i < len(s) and s[i] in valid_digits:
        if result > int(INT_MAX / 10) or (result == int(INT_MAX /10) and int(s[i]) > 7):
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + int(s[i])
        i += 1
    return result * sign

print(myAtoi('2147483648'))