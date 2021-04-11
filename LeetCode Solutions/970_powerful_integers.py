"""

Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.

TC = O (N square)
"""

def powerfulIntegers (x, y, bound):
    resultArray = []
    p1, p2 = 0 , 0
    for p1 in range(0,100):
        for p2 in range(0,100):
            resultado = x ** p1 + y ** p2
            if resultado <= bound and resultado not in resultArray:
                resultArray.append(resultado)
    return resultArray


x = 2
y = 3
bound = 10

print(powerfulIntegers(x,y,bound))
