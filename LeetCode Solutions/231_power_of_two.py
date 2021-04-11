"""
Solution: take 2 and start powerint to itself until the result is equal to n in which case we return true or the result is grater
than n in which case we return false

Steps:
- Check if is 1 or 2 and return True
- Set a variable result = 2
- Set a while to keep multiplying resultado for 2 until resultado is less than n
- if resultado = n return true
- if we get out of the loop then return false
"""

def isPowerOfTwo(n):
    if n==1 or n==2:
        return True
    resultado = 2
    while resultado < n:
        resultado = resultado * 2
        if resultado == n:
            return True
    return False

print (isPowerOfTwo(64))