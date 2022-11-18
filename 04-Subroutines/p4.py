def isInRange(n, x, y):
    
    if x <= n <= y:
        return True
    else:
        return False

print(isInRange(23, 1, 35))