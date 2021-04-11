"""
Statement: Given an integer n, return true if it is a power of three. Otherwise, return false.

Solution:
- Create a total variable equals 1
- Loop while total is less than n
- if total equals n return True
- if the program gets out of the loop return false

"""

def powerthree(n: int):
    """
    Confirms if an integer is a power of 3
    Parameters: n as integer
    Returns a boolean
    """
    if n == 0:
        return False
    if n == 1:
        return True
    total = 1
    while total < n:
        total = total * 3
        if total == n:
            return True
    return False

print(powerthree(45))