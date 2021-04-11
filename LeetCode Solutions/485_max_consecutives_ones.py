def max_consecutives_ones(nums):
    total = 0
    total_max = 0
    for n in nums:
        if n == 1:
            total += 1
        else:
            if total > total_max:
                total_max = total
            total = 0
    return total if total > total_max else total_max