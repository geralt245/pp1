def sum(n):
    if n > 0:
        n += sum(n - 1)
    return n

print(sum(10))