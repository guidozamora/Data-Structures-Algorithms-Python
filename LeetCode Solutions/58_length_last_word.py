"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

Time Complexity: O(N) where N is the number of characters in the string
Space Complexity: O(1)
"""
def length_last_word(s):
    cont = 0
    word_found = False

    for i in reversed(range(0,len(s))):
        if s[i] != ' ':
            cont += 1
            word_found = True
        elif word_found:
            break
    return cont

if __name__ == '__main__':
    
    s = ' '
    print(length_last_word(s))