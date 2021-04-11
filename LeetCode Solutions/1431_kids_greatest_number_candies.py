'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them
Notice that multiple kids can have the greatest number of candies.

[2,3,5,1,3]


Time Complexity:
Space Complexity:

'''

def kids_with_candies(candies, extra_candies):
    kid_more_candies = max(candies)
    answer = []

    for candy in candies:
        if candy + extra_candies >= kid_more_candies:
            answer.append(True)
        else:
            answer.append(False)
    return answer


if __name__ == "__main__":

    candies = [12,1,12]

    print(kids_with_candies(candies,extra_candies=10))