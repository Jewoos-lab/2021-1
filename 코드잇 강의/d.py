def sum_a(n):
    if n < 2:
        return n
    else:
        return 1/n + sum_a(n-1)
print(sum_a(3))
