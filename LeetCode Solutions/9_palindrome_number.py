def is_Palindrome(x):
    
    if x < 0:
        return False

    temp_num = x
    reverse_num = 0

    while temp_num > 0:
        reverse_num = reverse_num * 10 + temp_num % 10
        temp_num = temp_num // 10

    return reverse_num == x
    


if __name__ == '__main__':

    num = 121
    print(is_Palindrome(num))