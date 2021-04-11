"""
Given a string with a roman number return its int value

Solution
- Create a dictionary with the roman symbols as the key and the number as value
- Loop through the string and assign the number to its correspondent roman value
- If the value in the next position is higher than the value in the current position, then multiply it by -1 
- Sum the value to the total

Time Complexity = O(1) String will be 15 characters max because that is the highest roman number
Space Complexity = O(1) Just 4 variables no matter what the size of the array


"""

def romanToInt(s):
    numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    pos = 0
    
    while pos <= len(s) -1 :
        num = numbers[s[pos]]
        if pos <= len(s) - 2:
            if numbers[s[pos]] < numbers[s[pos+1]]:
                num = num * -1
        result += num
        pos += 1
    return result

if __name__=='__main__':
    s='MCMXCIV'
    print(romanToInt(s))