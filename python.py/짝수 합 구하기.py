def sum_even_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total = total + i
    return total
sum_even_numbers(9)
