
def maximumWealth(accounts):
    max = 0
    customer_wealth = 0
    for customer in accounts:
        for money in customer:
            customer_wealth += money
        if customer_wealth > max:
            max = customer_wealth
        customer_wealth = 0
    return max

print(maximumWealth([[1,2,3],[5,5,5]]))
