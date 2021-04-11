"""
Statement: Given a 32-bit signed integer, reverse digits of an integer

Solution:
- If number < 0 set flag negative flag to true and convert the number to positive
- Take the number and convert it to string
- Revert the string
- Convert the string to number
- If negative flag is True add a minus at the begining of the number
"""

def reverse_integer(x: int):
    """
    Given a 32-bit integer the function reverse the digits of the integer
    Parameters: x as int. The number you want to reverse the digits
    Returns: the reverse number
    """
    
    negative_number = False
    if x < 0:
        negative_number = True
        x = x * -1
    string_numero = str(x)
    reverse_string = string_numero[::-1]
    if negative_number:
        reverse_string = '-' + reverse_string
    reverse_number = int(reverse_string)
    if (-2**31) <= reverse_number <= (2**31 - 1):
        return reverse_number
    else:
        return 0


print(reverse_integer(1534236469))
