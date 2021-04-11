"""

TC = O(N)
SP = O()
"""
def balance_string (s):
    balanced_strings = 0
    sub_string = False
    number_L = 0
    number_R = 0
    previous_letter = s[0]

    for letter in s:
        if letter == 'R':
            number_R +=1
        else:
            number_L += 1

        if previous_letter != letter:
            sub_string = True
        if sub_string and number_L == number_R:
            balanced_strings += 1
            number_L = 0
            number_R = 0
            sub_string = False
        previous_letter = letter
    return balanced_strings

       
print (balance_string('RLRRLLRLRL'))