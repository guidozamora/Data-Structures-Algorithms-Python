"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""


if __name__ == '__main__':
    expenses = [2200,2350,2600,2130,2190]

    # 1. In Feb, how many dollars you spent extra compare to January?
    print(f'In feb I spend {expenses[1] - expenses[0]} dollars compared to Jan')

    #2. Find out your total expense in first quarter (first three months) of the year.
    print(f'Total expenses of the first quater are: {expenses[0] + expenses[1] + expenses[2]}')

    #3. Find out if you spent exactly 2000 dollars in any month
    if 2000 in expenses:
        print('I did spend exactly $2000 in any month')
    else:
        print('I did NOT spend exactly $2000 in any month')

    #4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    expenses.insert(5,1980)
    print(f'Expenses for June: {expenses[5]}')

    #5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
    expenses[3] = expenses[3] - 200
    print(f'Corrected expense for April is {expenses[3]}')



