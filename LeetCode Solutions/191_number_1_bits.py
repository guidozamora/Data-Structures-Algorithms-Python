"""
Statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Solution:
Loop thru the string and count the values different to 1
Use the count function

"""

def hamming_weight(binary_number):
    return binary_number.count('1')



print(hamming_weight('00000000000000000000000000001011'))