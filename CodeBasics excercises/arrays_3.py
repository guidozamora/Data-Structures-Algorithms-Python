"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

"""

def list_odd(max):
    odds = []
    
    for num in range(max):
        if num % 2 is not 0:
            odds.append(num)
    return odds

if __name__ == "__main__":

    print (list_odd(15))