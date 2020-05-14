def recursion(n):
    if n < 2:
        return 1
    return n * recursion(n-1)
recursion(980)