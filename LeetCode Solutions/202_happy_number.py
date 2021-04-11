"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and f

Solution

- While True
- Make an array of the digits of the numbers
- Loop thru each digit and store the square results of they array in a new variable
- Check if the variable value = 1 and return True
- Pending to confirm when to break the first loop
"""


def is_happy(n: int):
    resultado = n
    iterations = 0
    while True:
        string_number = str(resultado)
        resultado = 0
        iterations += 1
        for number in string_number:
            resultado = resultado + (int(number) **2)
        if resultado == 1:
            return True
        if iterations == 1000:
            return False    

print(is_happy(2))