"""
Receive an integer number and return its roman number
Max number should be 3999

Solution
- Check if 0 > number > 3999 and return -1
- Create dictionaries with each roman element
- Split each number digit and return it's roman representation

Time Complexity: O(1) worst case scenario the number will have 4 digits
Space Complexity: O(1) same 3 variables are created every time the program is executed
"""
def return_roman(number):
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']

    return thousands[number//1000] + hundreds[number%1000//100] + tens[number%100//10] + units[number%10]
    
if __name__=='__main__':
    
    number = 20
    print(return_roman(number))