"""
Statement: Given an integer n return true if it is a power of four, otherwise return false

Solution:
- Create a total variable and set it to four
- Create a loop and multiply total by four
- If total is equal to four return True
- Evaluate if total is greater than n if yes return False

"""
def powerfour(n: int):
    """
    Evaluates if an integer n is a power of four
    Parameters: integer n
    Return: True if n is power of four, otherwise False
    """
    total = 1
    if n == 1 or n == 4:
        return True
    while total < n:
        total = total * 4
        if total == n:
            return True
    return False


print(powerfour(64))
print(powerfour)


print()
