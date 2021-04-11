"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Time Complexity: O(n * m)
Space Complexity: O(1)

"""
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ''

    if len(strs) == 1:
        return strs[0]

    prefix = strs[0]
    lenght_prefix = len(prefix)    
    
    for s in strs[1:]:
        while prefix != s[0:lenght_prefix]:
            prefix = prefix[0:lenght_prefix-1]
            lenght_prefix -= 1

            if prefix == 0:
                return ''
    return prefix

if __name__ == "__main__":
    array_strings = []

    print(longest_common_prefix(array_strings))
